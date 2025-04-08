# Generated by Django 4.2.7

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
        ('users', '0002_followedcompany_savedjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managers', to='companies.company'),
        ),
    ]
