from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateField(auto_now_add=True)
    end = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.title
class Phase(models.Model):
    pass

class TeamRecord(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    start = models.DateField(auto_now_add=True)
    end = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    member = models.ManyToManyField(User, related_name='team_record')

    def __str__(self):
        return '{} - Team Record'.format(self.project.title)
    #member = models.ManyToMany(User, on_delete=models.CASCADE)

class Task(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    to_do = 'to do'
    done = 'done'
    in_progress = 'in progress'
    to_be_corrected = 'to be corrected'
    status_choices = [
        (to_do, 'to do'),
        (done, 'done'),
        (in_progress, 'in progress'),
        (to_be_corrected, 'to be corrected'),
    ]
    status = models.CharField(
        max_length=20,
        choices=status_choices,
        default=to_do,
    )

    def __str__(self):
        return '{} - {} '.format(self.project, self.title)
