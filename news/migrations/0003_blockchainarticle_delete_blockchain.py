# Generated by Django 5.0.6 on 2024-06-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_blockchain'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockChainArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='blockchain',
        ),
    ]
