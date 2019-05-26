from django.contrib import admin
from .models import Project, Phase, TeamRecord, Task
# Register your models here.

admin.site.register(Project)
admin.site.register(Phase)
admin.site.register(TeamRecord)
admin.site.register(Task)
