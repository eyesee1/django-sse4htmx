from typing import ClassVar

from django.core.exceptions import ImproperlyConfigured
from django.template.loader import get_template
from django_eventstream import send_event


class ServerSentEventHTMLFragmentSender:
    """
    A class for sending HTML fragments to the client using EventStream.
    """

    default_context: ClassVar[dict] = {}
    template_name: ClassVar[str] = ""
    channel_name: ClassVar[str] = ""
    event_type: ClassVar[str] = "message"

    def __init__(self):
        self.kwargs = self.default_context.copy()

    def __call__(self, **kwargs):
        """
        All extra keyword args will be available in the template context.
        """
        self.kwargs.update(kwargs)
        self._send_event()

    def _send_event(self):
        channel_name = self.get_channel_name()
        template_name = self.get_template_name()
        template = get_template(template_name)
        context_data = self.get_context_data()
        html = template.render(context_data)
        event_type = self.get_event_type()
        data = self._format_payload(html, event_type)
        send_event(channel_name, event_type, data, json_encode=False)

    @staticmethod
    def _format_payload(html, event_type):
        data = " ".join(line.strip() for line in html.strip().splitlines())
        if event_type == "message":
            return data

        return f"event: {event_type}\ndata: {data}\n\n"

    def get_template_name(self):
        if not self.template_name:
            msg = "Please set the template_name class variable or override get_template_name"
            raise ImproperlyConfigured(msg)

        return self.template_name

    def get_channel_name(self):
        if not self.channel_name:
            msg = "Please set the channel_name class variable or override get_channel_name"
            raise ImproperlyConfigured(msg)

        return self.channel_name

    def get_event_type(self):
        if not self.event_type:
            msg = "Please set the event_type class variable or override get_event_type"
            raise ImproperlyConfigured(msg)

        return self.event_type

    def get_context_data(self):
        return self.kwargs.copy()
