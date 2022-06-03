# Generated by Django 4.0.3 on 2022-03-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('specialization', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
                ('review', models.TextField(max_length=1000)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]