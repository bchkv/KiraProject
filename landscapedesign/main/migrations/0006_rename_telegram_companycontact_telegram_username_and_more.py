# Generated by Django 4.2.13 on 2024-05-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_companycontact_telegram_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companycontact',
            old_name='telegram',
            new_name='telegram_username',
        ),
        migrations.RenameField(
            model_name='companycontact',
            old_name='whatsapp',
            new_name='whatsapp_phone',
        ),
        migrations.AddField(
            model_name='companycontact',
            name='telegram_link',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='companycontact',
            name='whatsapp_link',
            field=models.URLField(blank=True),
        ),
    ]
