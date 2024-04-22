# Generated by Django 5.0.1 on 2024-01-15 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executive', '0011_auto_20240116_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableSeven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workload_faculty', models.CharField(max_length=50)),
                ('workload_semester', models.CharField(max_length=50)),
                ('workload_course', models.CharField(max_length=50)),
                ('workload_types', models.CharField(max_length=100)),
                ('workload_duties', models.CharField(max_length=100)),
                ('workload_total', models.IntegerField(default=0)),
            ],
        ),
    ]