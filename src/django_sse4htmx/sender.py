from typing import ClassVar

from django.core.exceptions import ImproperlyConfigured
from django.template.loader import get_template
from django_eventstream import send_event


class SSEFragmentSender:
    """
    A class for sending HTML fragments as Server Sent Events to the client using EventStream.
    """

    channel_name: ClassVar[str] = ""
    event_type: ClassVar[str] = "message"
    extra_context: ClassVar[dict] = {}
    template_name: ClassVar[str] = ""

    def send(self, **kwargs):
        """
        A convenience method for sending a message, for those who prefer to use a named method.
        """
        self.__call__(**kwargs)

    def __call__(self, **kwargs):
        """
        All keyword args will be made available in the template context.
        """
        self._send_event(**kwargs)

    def _send_event(self, **kwargs):
        channel_name = self.get_channel_name()
        template_name = self.get_template_name()
        template = get_template(template_name)
        context_data = self.get_context_data(**kwargs)
        event_type = self.get_event_type()
        data = template.render(context_data)
        send_event(channel_name, event_type, data, json_encode=False)

    def get_template_name(self):
        if not self.template_name:
            msg = (
                f"{self.__class__.__name__}: Please set the template_name class variable or "
                f"override get_template_name"
            )
            raise ImproperlyConfigured(msg)

        return self.template_name

    def get_channel_name(self):
        if not self.channel_name:
            msg = (
                f"{self.__class__.__name__}: Please set the channel_name class variable or "
                f"override get_channel_name"
            )
            raise ImproperlyConfigured(msg)

        return self.channel_name

    def get_event_type(self):
        if not self.event_type:
            msg = (
                f"{self.__class__.__name__}: Please set the event_type class variable or "
                f"override get_event_type"
            )
            raise ImproperlyConfigured(msg)

        return self.event_type

    def get_context_data(self, **kwargs):
        data = self.extra_context.copy()
        data.update(kwargs)
        return data
