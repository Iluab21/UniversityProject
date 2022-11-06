from django.db import models
from django.core.validators import ValidationError, RegexValidator
from django.contrib.auth.models import AbstractUser


def restrict_amount(value):
    if Student.objects.filter(studygroup=value).count() >= 20:
        raise ValidationError('Group already has maximal amount of sudents (20)')


class Direction(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)


class Curator(AbstractUser):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, null=True)

    def __str__(self):
        if not self.username:
            return ""
        return str(self.username)


class Discipline(models.Model):
    name = models.CharField(max_length=255)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)


class StudyGroup(models.Model):
    name = models.CharField(max_length=255)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)


class Student(models.Model):
    name = models.CharField(max_length=255)
    studygroup = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, validators=(restrict_amount, ))

    phoneNumberRegex = RegexValidator(regex=r"^7?1?\d{10,10}$")
    phone = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True)

    GENDER = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField('Gender', choices=GENDER, max_length=2)

    def __str__(self):
        if not self.name:
            return ""
        return str(self.name)
