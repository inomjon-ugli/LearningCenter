from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        TEACHER = 'teacher', 'Teacher'
        STUDENT = 'student', 'Student'

    full_name = models.CharField(max_length=220)
    phone = models.CharField(max_length=13)

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT
    )


    student_group = models.ForeignKey(
        'groups.Group',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='students'
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'custom_user'

    def __str__(self):
        return f"{self.full_name} ({self.role})"
