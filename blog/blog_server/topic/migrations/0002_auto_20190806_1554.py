# Generated by Django 2.2.2 on 2019-08-06 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='author',
            field=models.ForeignKey(on_delete=False, to='user.UserProfile'),
        ),
    ]
