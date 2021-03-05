from rest_framework import serializers

from . import models

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Student
        fields = ['firstname', 'surname', 'gender', 'age']