# Generated by Django 4.1.5 on 2023-01-22 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_rename_p_category_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='couser',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='couser',
            name='image',
            field=models.ImageField(default=None, upload_to='courses/%Y/%m'),
        ),
        migrations.AlterUniqueTogether(
            name='couser',
            unique_together={('subject', 'Category')},
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('image', models.ImageField(default=None, upload_to='courses/%Y/%m')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('content', models.TextField()),
                ('Couser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.couser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
