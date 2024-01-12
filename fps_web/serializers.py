from rest_framework import serializers
from executive.models import TableTwo

class TableTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableTwo
        fields = ['id', 'faculty_no', 'training_title', 'description','training_date', 'training_time', 'duration', 'location']