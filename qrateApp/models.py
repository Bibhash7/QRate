from django.db import models
from django.utils.text import slugify
import uuid

class CodeSnippet(models.Model):
    code = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(uuid.uuid4().hex[:8])
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

