from django.db import models

# Create your models here.

class SecretariatMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='secretariat/')
    bio = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.role})"

class ExecutiveBoardMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='eboard/')
    bio = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.role})"

class Committee(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='committees/')
    short_description = models.CharField(max_length=255)
    agenda = models.CharField(max_length=255)
    background_guide = models.FileField(upload_to='background_guides/')
    venue = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CommitteeMember(models.Model):
    committee = models.ForeignKey(Committee, related_name='members', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=[('Chair', 'Chair'), ('Vice-Chair', 'Vice-Chair')])

    def __str__(self):
        return f"{self.name} ({self.role}) - {self.committee.name}"

class ItineraryEvent(models.Model):
    DAY_CHOICES = [(1, 'Day 1'), (2, 'Day 2')]
    day = models.IntegerField(choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['day', 'start_time']

    def __str__(self):
        return f"Day {self.day} - {self.start_time.strftime('%H:%M')} to {self.end_time.strftime('%H:%M')}: {self.title}"

class GalleryImage(models.Model):
    CHAPTER_CHOICES = [(1, 'Chapter 1 (2024)'), (2, 'Chapter 2 (2025)')]
    chapter = models.IntegerField(choices=CHAPTER_CHOICES)
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Chapter {self.chapter}: {self.caption or self.image.name}"

class ResourceLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    pdf = models.FileField(upload_to='resources/', blank=True, null=True)

    def __str__(self):
        return self.title

class Signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    school = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.school})"
