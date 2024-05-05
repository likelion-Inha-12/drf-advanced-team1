from django.db import models

class Category(models.Model):
    tag = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.tag

class Assignment(models.Model):
    PART_OPTION = (
        ('ALL', 'ALL'),
        ('FE', 'FE'),
        ('BE', 'BE'),
    )
    title = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    part = models.CharField(max_length=20, choices=PART_OPTION)
    tag_id = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE, related_name="assignments")
    link = models.URLField()
    content = models.TextField(max_length=200)

    def __str__(self):
        return self.title


class Memeber(models.Model):
    name = models.CharField(max_length=20)


class Submission(models.Model):
    content = models.CharField(max_length=200)
    link = models.URLField()
    create_at = models.DateTimeField(auto_now_add=True)
    member_id = models.ForeignKey(Memeber, verbose_name="Member",on_delete=models.CASCADE, related_name="submissions")
    assignment_id = models.ForeignKey(Assignment, verbose_name="Assignment", on_delete=models.CASCADE, related_name="submissions", null=True)

# Create your models here.
