# Generated by Django 2.0 on 2019-03-16 09:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20190312_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=150)),
                ('Description', models.TextField(blank=True)),
                ('Status', models.CharField(choices=[('INPROGRESS', 'Inprogress'), ('NOT ASSIGNED', 'Not assigned'), ('DONE', 'done'), ('PLANNED', 'Planned')], default='NOT ASSIGNED', max_length=50)),
                ('Time', models.DateTimeField(default=django.utils.timezone.now)),
                ('Assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.SignUp')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Creator_name', models.CharField(max_length=120)),
                ('Team_Name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1024)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('members', models.ManyToManyField(to='manager.SignUp')),
            ],
        ),
    ]