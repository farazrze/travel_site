# Generated by Django 5.0.3 on 2024-03-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_options_post_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_date'], 'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/defualt.jpg', upload_to='blog/'),
        ),
    ]