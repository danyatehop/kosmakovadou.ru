# Generated by Django 4.1.7 on 2023-03-15 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_delete_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Заголовок страницы')),
                ('description', models.CharField(max_length=500, verbose_name='Краткое описание страницы')),
                ('text', models.TextField(max_length=5000, verbose_name='Содержимое страницы')),
                ('section_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.section')),
            ],
        ),
    ]
