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

    
class TableThree(models.Model):
    faculty_no = models.CharField(max_length=10)
    training_title = models.CharField(max_length=100)
    description = models.TextField()
    training_date = models.CharField(max_length=120)
    training_time = models.CharField(max_length=120)
    duration = models.CharField(max_length=20)
    location = models.CharField(max_length=50)


    # @classmethod
    # def insert_data(cls):
    #     data = [
    #         ["01", "Effective Teaching Strategies", "Innovative pedagogical approaches, Active learning techniques, Flipped classroom methodologies", "2023-11-15", "3:00 - 4:30 PM", "3 Days", "PUPQC - Gymnasium"],
    #         ["02", "Technology Integration", "Integrating technology into the curriculum, Online teaching best practices, Utilizing learning management systems effectively", "2023-01-13", "10:00 - 11:30 PM", "3 Days", "PUPQC - Gymnasium"],
    #         ["03", "Research Skills", "Research methodologies and design, Grant writing and funding opportunities, Publication strategies", "2023-08-28", "3:00 - 4:30 PM", "3 Days", "PUPQC - Gymnasium"],
    #         ["04", "Inclusive Teaching", "Culturally responsive teaching, Creating an inclusive classroom environment, Addressing diverse learning styles", "2023-09-04", "3:00 - 4:30 PM", "3 Days", "PUPQC - Gymnasium"],
    #         ["05", "Communication Skills", "Effective communication with students and colleagues, Public speaking and presentation skills, Writing for academic and non-academic audiences", "2023-07-20", "10:00 - 11:30 PM", "3 Days", "PUPQC - Gymnasium"],
    #         ["06", "Leadership and Management", "Academic leadership skills, Team building and collaboration, Conflict resolution and management", "2023-04-29", "9:00 - 10:30 PM", "3 Days", "PUPQC - Gymnasium"],
    #         ["07", "Professional Networking", "Building and maintaining a professional network, Attending conferences and academic events, Online networking strategies", "2023-01-13", "9:00 - 10:30 PM", "3 Days", "PUPQC - Gymnasium"],
    #     ]

    #     for item in data:
    #         cls.objects.create(
    #             faculty_no=item[0],
    #             training_title=item[1],
    #             description=item[2],
    #             training_date=item[3],
    #             training_time=item[4],
    #             duration=item[5],
    #             location=item[6],
    #         )

# TableThree.insert_data()
