from django.db import models
from django.utils.timezone import now #생성 시간

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    PART_OPTION = (
        ('ALL', 'ALL'),
        ('FE', 'FE'),
        ('BE', 'BE'),
    )
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    part = models.CharField(max_length=3, choices=PART_OPTION)
    tag = models.ForeignKey(Category, verbose_name="Category", on_delete=models.SET_NULL, related_name="assignments", null=True)
    # 과제가 삭제되더라도 tag 값은 남아있게 하기 위해서 on_delete옵션을 SET_NULL로 해주었습니다!
    link = models.URLField()
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.title

# class Member(models.Model):
#     name = models.CharField(max_length=20)
# member 클래스의 필요성을 느끼지 못해서 일단 주석처리 했습니다

class Submission(models.Model):
    content = models.CharField(max_length=200)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    #member_id = models.ForeignKey(Member, verbose_name="Member",on_delete=models.CASCADE, related_name="submissions")
    assignment_id = models.ForeignKey(Assignment, verbose_name="Assignment", on_delete=models.CASCADE, related_name="submissions", null=True)

# Create your models here.
