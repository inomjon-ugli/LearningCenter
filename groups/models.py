from django.db import models
from django.conf import settings

class Group(models.Model):
    class Schedule(models.TextChoices):
        MONDAY = 'monday', 'Monday'
        TUESDAY = 'tuesday', 'Tuesday'
        WEDNESDAY = 'wednesday', 'Wednesday'
        THURSDAY = 'thursday', 'Thursday'
        FRIDAY = 'friday', 'Friday'
        SATURDAY = 'saturday', 'Saturday'
        SUNDAY = 'sunday', 'Sunday'

    group_name = models.CharField(max_length=200)

    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='groups',
    )

    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'teacher'},
        related_name='teaching_groups'
    )

    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)

    schedule = models.CharField(
        max_length=20,
        choices=Schedule.choices,
        default=Schedule.MONDAY
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.group_name} ({self.course})"
