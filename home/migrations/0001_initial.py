# Generated by Django 3.1.1 on 2021-03-30 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jobregisteration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=122)),
                ('lastname', models.CharField(max_length=122)),
                ('DOB', models.CharField(max_length=12)),
                ('place', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('blank1', models.TextField()),
                ('blank2', models.TextField()),
                ('blank3', models.TextField()),
                ('blank4', models.TextField()),
                ('blank5', models.TextField()),
                ('blank6', models.TextField()),
                ('blank7', models.TextField()),
                ('blank8', models.TextField()),
                ('blank9', models.TextField()),
                ('blank10', models.TextField()),
                ('blank11', models.TextField()),
                ('data', models.DateField()),
            ],
        ),
    ]
