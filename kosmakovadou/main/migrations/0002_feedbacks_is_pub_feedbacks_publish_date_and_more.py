# Generated by Django 4.1.7 on 2023-02-28 04:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacks',
            name='is_pub',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='feedbacks',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации отзыва'),
        ),
        migrations.AlterField(
            model_name='feedbacks',
            name='feedback_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата отправки отзыва'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=15, verbose_name='Фамилия')),
                ('firstname', models.CharField(max_length=15, verbose_name='Имя')),
                ('middlename', models.CharField(max_length=15, verbose_name='Отчество')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Адрес электронной почты')),
                ('phone', models.CharField(blank=True, max_length=10, verbose_name='Номер телефона')),
                ('body', models.TextField(verbose_name='Ваш комментарий')),
                ('feedback_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата отправки отзыва')),
                ('publish_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации отзыва')),
                ('is_pub', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.articles')),
            ],
        ),
    ]
