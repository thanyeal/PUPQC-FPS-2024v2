# Generated by Django 4.2.6 on 2023-11-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('executive', '0007_auto_20231121_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableFive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merit_faculty_name', models.CharField(max_length=50)),
                ('merit_faculty_status', models.CharField(max_length=50)),
                ('merit_ave_dept_rate', models.DecimalField(max_digits=4, decimal_places=2, default=0.00)),
                ('merit_rsrch_publish', models.CharField(max_length=200)),
                ('merit_training_attended', models.CharField(max_length=100)),
                ('merit_promotion', models.BooleanField()),
            ],
        ),
    ]