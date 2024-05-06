from rest_framework import serializers
from .models import Assignment, Submission, Category
from django.utils import timezone #생성 시간


class SubmissionSerializer(serializers.ModelSerializer):
    submitted_at = serializers.DateTimeField(source='created_at')  # 제출물 작성 일자
    class Meta:
        model = Submission
        fields = ["content", "link", "create_at"]


class AssignmentPostSerializer(serializers.ModelSerializer):
    # 과제물 생성시 사용할 serializer입니다.
    tag = serializers.CharField(required=True)
    # 태그란에 필수로 입력해야 하는걸로 해놨습니다

    class Meta:
        model = Assignment
        fields = ['title', 'deadline', 'part', 'tag', 'link', 'content']
        # 이 필드 부분때문에 생성시 사용할 serializer를 따로 만들었습니다



class AssignmentSerializer(serializers.ModelSerializer):
     #과제 조회 시 사용할 serializer입니다.
     tag = serializers.CharField(source='tag.name') #태그 이름 가져오기
     submissions = SubmissionSerializer(many=True, read_only=True)
     time_left = serializers.SerializerMethodField() #과제 마감까지 남은 시간
     submissions_count = serializers.SerializerMethodField(read_only=True) #과제 제출물 개수

     def get_time_left(self, obj):
        # 남은 시간을 계산하는 메소드입니다.
        deadline = obj.deadline
        now_time = timezone.now().date()
        time_diff = deadline - now_time
        return max(time_diff.days, 0)  # 남은 일수를 반환, 이미 마감된 경우 0을 반환.
        
     def get_submissions_count(self, obj):
            # 제출물의 수를 계산하는 메소드입니다.
            return obj.submissions.count()

     class Meta:
        model = Assignment
        fields = ['title', 'create_at', 'part', 'tag', 'time_left', 'link', 'content', 'submissions', 'submissions_count']