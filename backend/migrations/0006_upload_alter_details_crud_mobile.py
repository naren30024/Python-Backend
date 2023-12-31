# Generated by Django 4.1.7 on 2023-10-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_details_crud_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.AlterField(
            model_name='details_crud',
            name='mobile',
            field=models.PositiveBigIntegerField(),
        ),
    ]
