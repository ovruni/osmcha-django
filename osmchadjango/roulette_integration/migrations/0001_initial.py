# Generated by Django 2.2.11 on 2020-06-01 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('changeset', '0050_auto_20181008_1001'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeIntegration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_id', models.IntegerField(db_index=True, unique=True)),
                ('active', models.BooleanField(db_index=True, default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reasons', models.ManyToManyField(related_name='challenges', to='changeset.SuspicionReasons')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challenges', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Challenge Integration',
                'verbose_name_plural': 'Challenge Integrations',
                'ordering': ['id'],
            },
        ),
    ]