from django.db import models
from apps.login_registration_app.models import *

# Create your models here.
class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="messages")

    def __repr__(self):
        return f"<Message object: {self.id}>"

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="comments_from_user")
    message = models.ForeignKey(Message, related_name="comments_on_message")

    def __repr__(self):
        return f"<Message object: {self.id}>"
