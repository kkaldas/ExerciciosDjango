# Generated by Django 3.0 on 2019-12-17 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Usuario',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='password',
            new_name='senha',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='username',
            new_name='usuario',
        ),
    ]