from __future__ import unicode_literals

from django.db import models


# Create your models here.

class UsernamesManager(models.Manager):
    def add(self, username):
        print len(username)
        messages = []
        if len(username) < 8:
            messages.append('Username must be longer than 8 characters')
        if len(username) > 25:
            messages.append('Username must be fewer than 26 characters')
        
        if len(messages) > 0:
            return False, messages
        else:
            username = Usernames.usernamesManager.create(username=username)
            return (True, username)


class Usernames(models.Model):
    username = models.CharField(max_length=30)
    usernamesManager = UsernamesManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


