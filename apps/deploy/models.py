from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Deployment(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    image = models.ImageField(upload_to='deployments/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name) or 'deployment'
            candidate_slug = base_slug
            index = 2

            while Deployment.objects.filter(slug=candidate_slug).exclude(pk=self.pk).exists():
                candidate_slug = f'{base_slug}-{index}'
                index += 1

            self.slug = candidate_slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('deploy:deployment_detail', kwargs={'d_slug': self.slug})