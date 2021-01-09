# Generated by Django 3.1.2 on 2021-01-07 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strolchibot', '0004_linkpermit'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkBlacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='LinkWhitelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='twitchuser',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]