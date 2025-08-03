from django.db import models
from django.utils.text import slugify


class Course(models.Model):
    class LevelChoices(models.TextChoices):
        BEGINNER = 'beginner', 'Beginner'
        INTERMEDIATE = 'intermediate', 'Intermediate'
        ADVANCED = 'advanced', 'Advanced'

    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=320, unique=True, blank=True)
    description = models.TextField(verbose_name='Course Description')
    duration_course = models.PositiveSmallIntegerField(help_text='Duration in weeks')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    level = models.CharField(max_length=20, choices=LevelChoices.choices, default=LevelChoices.BEGINNER)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'courses'
        ordering = ['-created_at']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return f"{self.title} ({self.level})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


