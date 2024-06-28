import mongoengine
from django.utils import timezone


class PDFContent(mongoengine.Document):
    email = mongoengine.EmailField(required=True, unique=True)
    file = mongoengine.StringField(max_length=255)
    nouns = mongoengine.ListField()
    verbs = mongoengine.ListField()
    uploaded_at = mongoengine.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
