from faker import Faker

from django_sse4htmx import SSEFragmentSender

__all__ = ["default_sender", "named_sender", "wrong_named_sender"]

fake = Faker()


class DefaultMessageSender(SSEFragmentSender):
    channel_name = "default"
    template_name = "myapp/home.html#one-unnamed-message"


default_sender = DefaultMessageSender()


class NamedMessageSender(SSEFragmentSender):
    channel_name = "named"
    template_name = "myapp/home.html#one-named-message"
    event_type = "MyMessage"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["text"] = f"{fake.company()}: {fake.catch_phrase()}"
        return data


named_sender = NamedMessageSender()


class WrongNamedMessageSender(SSEFragmentSender):
    channel_name = "named"
    template_name = "myapp/home.html#one-named-message"
    event_type = "BogusMessage"


wrong_named_sender = WrongNamedMessageSender()
