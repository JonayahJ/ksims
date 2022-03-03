# Contact models
from django.db import models
from datetime import datetime

# Contact
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(null=True, blank=True, max_length=200)
    message = models.TextField(blank=True, null=True)
    sent_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email