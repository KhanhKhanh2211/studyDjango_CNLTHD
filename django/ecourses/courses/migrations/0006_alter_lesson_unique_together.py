# Generated by Django 4.1.5 on 2023-02-10 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_lesson_content'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('subject', 'Couser')},
        ),
    ]
