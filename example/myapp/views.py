from django.http import HttpResponse
from django.views.generic import FormView, TemplateView
from faker import Faker
from myapp.forms import SendEventForm
from myapp.senders import default_sender, named_sender, wrong_named_sender

fake = Faker()


class HomeView(TemplateView):
    template_name = "myapp/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "My App"
        return context


class SendAnEvent(FormView):
    success_url = "#"
    form_class = SendEventForm
    template_name = "myapp/home.html"

    def form_valid(self, form):
        message_type = form.cleaned_data["event_type"]
        text = fake.paragraph(nb_sentences=2)

        match message_type:
            case "message":
                default_sender(text=text)

            case "MyMessage":
                named_sender(text=text)

            case "BogusMessage":
                wrong_named_sender(text=text)

            case _:
                return HttpResponse("Error! Unknown message type.")

        return HttpResponse("Sent.")

    def form_invalid(self, form):
        return HttpResponse("NO!")
