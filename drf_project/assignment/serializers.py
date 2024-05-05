from rest_framework import serializers
from .models import Assignment, Submission


class SubmissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Submission
        fields = ["content", "link", "creat_at"]


# class AssignmentSerializer(serializers.ModelSerializer):
#     submissions = SubmissionSerializer(Submission)
#     time_left = 
#     submissions_count = 

#     class Meta:
#         model = Assignment
#         fields = 