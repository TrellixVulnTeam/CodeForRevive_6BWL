# Generated by Django 2.0 on 2019-03-16 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_task_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='Creator_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='manager.SignUp'),
        ),
    ]
