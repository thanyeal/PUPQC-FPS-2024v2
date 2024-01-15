from django.db import models
from django.utils import timezone

# Table 1 - Evaluations w/ Upload
class TableOne(models.Model):

    faculty_num = models.IntegerField(default=0)

    facultyname = models.CharField(max_length=50)

    spvs_rating = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00
    )
    spvs_interp = models.CharField(max_length=20)

    stud_rating = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00
    )
    stud_interp = models.CharField(max_length=20)

    peer_rating = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00
    )
    peer_interp = models.CharField(max_length=20)

    self_rating = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00
    )
    self_interp = models.CharField(max_length=20)
    
    load_rating = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00
    )
    load_interp = models.CharField(
        max_length=20,
        default=''
    )

    faculty_stat = models.CharField(
        max_length=15,
        default=''
    )

    semester = models.CharField(
        max_length=15,
        default=''
    )

    eval_year = models.DateTimeField(default=timezone.now)

# Table 2 and 3 - Professional Development
class TableTwo(models.Model):
    faculty_no = models.CharField(max_length=10)
    training_title = models.CharField(max_length=100)
    description = models.TextField()
    training_date = models.CharField(max_length=120)
    training_time = models.CharField(max_length=120)
    duration = models.CharField(max_length=20)
    location = models.CharField(max_length=50)

class TableThree(models.Model):
    faculty_name = models.CharField(max_length=100)
    time_in = models.TimeField()
    time_out = models.TimeField()
    training_title = models.CharField(max_length=100)

# Table 4- Research Informations
class TableFour(models.Model):
    rsrch_author = models.CharField(max_length=100)
    rsrch_title = models.CharField(max_length=200)
    rsrch_year = models.DateField()
    rsrch_publisher = models.CharField(max_length=100)
    rsrch_category = models.CharField(max_length=100)
    rsrch_author_type = models.CharField(max_length=50)

# Table 5 - Merit and Promotions
class TableFive(models.Model):
    merit_faculty_name      = models.CharField(max_length=50)
    merit_faculty_status    = models.CharField(max_length=50)
    merit_ave_dept_rate     = models.DecimalField(
                                max_digits=4,
                                decimal_places=2,
                                default=0.00
                                )
    merit_rsrch_publish     = models.CharField(max_length=200)
    merit_training_attended = models.CharField(max_length=100)
    merit_promotion         = models.BooleanField()

# Table 6 - Faculty Leave Mgmt.
class TableSix(models.Model):
    leave_faculty   = models.CharField(max_length=50)
    leave_type      = models.CharField(max_length=50)
    leave_start     = models.DateField()
    leave_end       = models.DateField()
    leave_duration  = models.IntegerField(default=0)
    leave_status    = models.CharField(max_length=20)

# Table 7 - Faculty Workload
class TableSeven(models.Model):
    workload_faculty    = models.CharField(max_length=50)
    workload_semester   = models.CharField(max_length=50)
    workload_course     = models.CharField(max_length=50)
    workload_types      = models.CharField(max_length=100)
    workload_duties     = models.CharField(max_length=100)
    workload_total      = models.IntegerField(default=0)

# Table 8 - Awards and Recognition
class TableEight(models.Model):
    awards_faculty  = models.CharField(max_length=50)
    awards_title    = models.CharField(max_length=50)
    awards_date     = models.DateField()
    awards_type     = models.CharField(max_length=50)
    awards_status   = models.CharField(max_length=300)
