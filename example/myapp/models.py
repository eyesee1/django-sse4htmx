from django.db import models


class EventTypes(models.TextChoices):
    UNNAMED_MESSAGE = "message"
    NAMED_MESSAGE = "MyMessage"
    BOGUS_MESSAGE = "BogusMessage"
