# Generated by Django 2.0 on 2019-03-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=100)),
                ('mobile_no', models.IntegerField(max_length=10)),
                ('password', models.CharField(max_length=40)),
                ('confrom_pass', models.CharField(max_length=40)),
            ],
        ),
    ]