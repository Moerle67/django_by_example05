from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(("Titel"), max_length=250)
    slug = models.SlugField(("Slug"), max_length=250)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name=("Autor"), 
        on_delete=models.CASCADE,
        related_name='blg_posts'
    )
    body = models.TextField(("Nachricht"))
    publish = models.DateTimeField(("Veröffentlicht"), default=timezone.now)
    creates = models.DateTimeField(("Erstellt"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(("Geändert"), auto_now=True, auto_now_add=False)
    status = models.CharField(
        "Zustand",
        max_length=2,
        choices=Status,
        default=Status.DRAFT
    )

    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        return self.title

"""     def get_absolute_url(self):
        return reverse("Post_detail", kwargs={"pk": self.pk})
 """