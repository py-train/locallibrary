# Generated by Django 4.2.7 on 2023-11-04 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_auto_20220222_0623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'), ('can_destroy_book', 'Destroy Book'))},
        ),
    ]
