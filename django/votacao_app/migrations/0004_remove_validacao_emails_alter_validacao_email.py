# Generated by Django 4.1.1 on 2023-06-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("votacao_app", "0003_emailconfirmacao"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="validacao",
            name="emails",
        ),
        migrations.AlterField(
            model_name="validacao",
            name="email",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
