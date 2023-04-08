# Generated by Django 4.1.6 on 2023-03-30 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=255, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='books',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='books',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.genres', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(upload_to='photos/bookphoto/%Y/%m/%d/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='books',
            name='pub_date',
            field=models.IntegerField(verbose_name='Год выпуска'),
        ),
        migrations.AlterField(
            model_name='books',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='books',
            name='title',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Название'),
        ),
    ]
