# Generated by Django 5.0.1 on 2024-01-11 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]