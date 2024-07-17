# Generated by Django 5.0.6 on 2024-07-15 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='image/', verbose_name='Логотип сайта')),
                ('banner', models.ImageField(upload_to='banner/', verbose_name='Фото баннера')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='Номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='instagram')),
                ('location', models.CharField(max_length=255, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Настройка сайта',
                'verbose_name_plural': 'Настройки сайта',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок новости')),
                ('image', models.ImageField(upload_to='news_image/', verbose_name='фото новости')),
                ('author', models.CharField(max_length=255, verbose_name='Автор новости')),
                ('about', models.CharField(max_length=255, verbose_name='Краткое описание новости')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Our_advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('title_ky', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Наши преимущества',
            },
        ),
        migrations.CreateModel(
            name='Our_chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя Шеф-повара')),
                ('type', models.CharField(max_length=255, verbose_name='Тип повара')),
                ('photo', models.ImageField(upload_to='photo_chef/', verbose_name='фото повара')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook - повара')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='youtube - повара')),
            ],
            options={
                'verbose_name': 'Повар',
                'verbose_name_plural': 'Повара',
            },
        ),
        migrations.CreateModel(
            name='Popular_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('description', models.CharField(max_length=255, verbose_name='Описание блюда')),
                ('photo', models.ImageField(upload_to='popular_category/', verbose_name='фото блюда')),
            ],
            options={
                'verbose_name': 'Популярная категория',
                'verbose_name_plural': 'Популярные категории',
            },
        ),
    ]