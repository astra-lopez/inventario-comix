# Generated by Django 5.0.6 on 2024-06-14 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_comics_sale_comic_ids_remove_sale_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='comic_ids',
            new_name='comics',
        ),
    ]