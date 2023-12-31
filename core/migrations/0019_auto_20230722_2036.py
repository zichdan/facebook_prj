# Generated by Django 3.2.18 on 2023-07-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_groupchat_groupchatmessage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessage',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Personal Chat'},
        ),
        migrations.AlterModelOptions(
            name='groupchat',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Group Chat'},
        ),
        migrations.AlterModelOptions(
            name='groupchatmessage',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Group Chat Messages'},
        ),
        migrations.AddField(
            model_name='groupchat',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
