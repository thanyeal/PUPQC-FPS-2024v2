from django.db import models
from django.utils import timezone

class TableOne(models.Model):

    faculty_num = models.IntegerField(
        default=0
    )

    facultyname = models.CharField(
        max_length=50
    )

    spvs_rating = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00
    )
    spvs_interp = models.CharField(
        max_length=20
    )

    stud_rating = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00
    )
    stud_interp = models.CharField(
        max_length=20
    )

    peer_rating = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00
    )
    peer_interp = models.CharField(
        max_length=20
    )

    self_rating = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.00
    )
    self_interp = models.CharField(
        max_length=20
    )
    
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

    eval_year = models.DateTimeField(
        default=timezone.now
    )
