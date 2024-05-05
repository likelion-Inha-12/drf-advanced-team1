from rest_framework import serializers
from .models import Assignment, Submission


class SubmissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Submission
        fields = ["content", "link", "creat_at"]


class AssignmentPostSerializer(serializers.ModelSerializer):
    # 과제물 생성시 사용할 serializer입니다.
    tag = serializers.CharField(required=True)
    # 태그란에 필수로 입력해야 하는걸로 해놨습니다

    class Meta:
        model = Assignment
        fields = ['title', 'deadline', 'part', 'tag', 'link', 'content']
        # 이 필드 부분때문에 생성시 사용할 serializer를 따로 만들었습니다



# class AssignmentSerializer(serializers.ModelSerializer):
# 이거는 뼈대 코드에 있던건데 과제 조회하거나 삭제 할 경우 사용하면 될거 같아요..!
#     submissions = SubmissionSerializer(Submission)
#     time_left = 0
#     submissions_count = 0 


#     class Meta:
#         model = Assignment
#         fields = 