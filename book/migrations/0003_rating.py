# Generated by Django 4.1.4 on 2022-12-26 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_updated_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=100)),
                ('choice_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_object', to='book.book')),
            ],
        ),
    ]
