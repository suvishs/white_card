# Generated by Django 4.1.7 on 2023-03-08 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whitecardapp', '0004_application_admin_approval'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='qr',
            field=models.ImageField(null=True, upload_to='qr_code'),
        ),
    ]
