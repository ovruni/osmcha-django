# Generated by Django 2.0.3 on 2018-03-07 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('changeset', '0048_changeset_area'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='suspicionreasons',
            options={'ordering': ['id'], 'verbose_name': 'Suspicion reason', 'verbose_name_plural': 'Suspicion reasons'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='userwhitelist',
            options={'ordering': ['-whitelist_user']},
        ),
    ]