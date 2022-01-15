from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class ShortUrls(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    prime_url = models.URLField(max_length=512)
    slug = models.CharField(max_length=16, null=True)

    def __str__(self):
        return self.prime_url
