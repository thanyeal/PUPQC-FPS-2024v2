# Generated by Django 5.0.1 on 2024-01-15 15:16

from django.db import migrations

def insert_data(apps, schema_editor):
    TableTwo = apps.get_model('executive', 'TableTwo')
    data = [
        ["01", "Effective Teaching Strategies"  , "Innovative pedagogical approaches, Active learning techniques, Flipped classroom methodologies"                                                  , "2023-11-15"  , "3:00 - 5:00 PM"  , "2 Hours" , "PUPQC - Gymnasium"   ],
        ["02", "Technology Integration"         , "Integrating technology into the curriculum, Online teaching best practices, Utilizing learning management systems effectively"                   , "2023-01-13"  , "10:00 - 11:00 PM", "1 Hour"  , "PUPQC - Comlab"      ],
        ["03", "Research Skills"                , "Research methodologies and design, Grant writing and funding opportunities, Publication strategies"                                              , "2023-08-28"  , "3:00 - 5:00 PM"  , "2 Hours" , "PUPQC - Gymnasium"   ],
        ["04", "Inclusive Teaching"             , "Culturally responsive teaching, Creating an inclusive classroom environment, Addressing diverse learning styles"                                 , "2023-09-04"  , "3:00 - 6:00 PM"  , "3 Hours" , "PUPQC - Comlab"      ],
        ["05", "Communication Skills"           , "Effective communication with students and colleagues, Public speaking and presentation skills, Writing for academic and non-academic audiences"  , "2023-07-20"  , "10:00 - 11:00 PM", "2 Hours" , "PUPQC - Comlab"      ],
        ["06", "Leadership and Management"      , "Academic leadership skills, Team building and collaboration, Conflict resolution and management"                                                 , "2023-04-29"  , "9:00 - 11:00 PM" , "2 Hours" , "PUPQC - Gymnasium"   ],
        ["07", "Professional Networking"        , "Building and maintaining a professional network, Attending conferences and academic events, Online networking strategies"                        , "2023-01-13"  , "9:00 - 12:00 PM" , "3 Hours" , "PUPQC - Comlab"      ],
    ]
    for item in data:
        TableTwo.objects.create(
            faculty_no=item[0],
            training_title=item[1],
            description=item[2],
            training_date=item[3],
            training_time=item[4],
            duration=item[5],
            location=item[6],
        )

class Migration(migrations.Migration):

    dependencies = [
        ('executive', '0002_tabletwo'),
    ]

    operations = [
        migrations.RunPython(insert_data),
    ]