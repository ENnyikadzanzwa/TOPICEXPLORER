from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    # LEMENTARY = "Elementary School"
    # HIGHSCHOOL = "High School"
    # COLLEGE = "College"
    # EDUCATION_LEVEL_CHOICES = {
    #     ELEMENTARY: "Elementary School",
    #     HIEGHSCHOOL : "High School",
    #     COLLEGE: "College",
    # }
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    education_level = models.CharField(max_length=20)
    # education_level = models.TextChoices(max_length=20,
    #     choices=EDUCATION_LEVEL_CHOICES,
    #     default=ELEMENTARY,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
