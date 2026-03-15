from django.db import migrations, models
from django.utils.text import slugify


def populate_deployment_slugs(apps, schema_editor):
    Deployment = apps.get_model('deploy', 'Deployment')
    used_slugs = set(
        Deployment.objects.exclude(slug__isnull=True)
        .exclude(slug='')
        .values_list('slug', flat=True)
    )

    for deployment in Deployment.objects.all().order_by('id'):
        if deployment.slug:
            continue

        base_slug = slugify(deployment.name) or 'deployment'
        candidate_slug = base_slug
        index = 2

        while candidate_slug in used_slugs:
            candidate_slug = f'{base_slug}-{index}'
            index += 1

        deployment.slug = candidate_slug
        deployment.save(update_fields=['slug'])
        used_slugs.add(candidate_slug)


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, null=True, unique=True),
        ),
        migrations.RunPython(populate_deployment_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='deployment',
            name='slug',
            field=models.SlugField(blank=True, max_length=140, unique=True),
        ),
    ]
