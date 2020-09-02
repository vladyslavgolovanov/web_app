from django.db import models


# Create your models here.
class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=124, unique=True, default=login)

    def get_publication(self):
        return Publication.objects.filter(profile_id=self.id)

    def __str__(self):
        return f'nickname - {self.nickname}, id - {self.id}, password - {self.password}'


class Publication(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comments = models.CharField(max_length=248, blank=True)
    contents = models.FileField(null=True, blank=True, upload_to="images")

    def __str__(self):
        return f'nickname - {self.profile_id}'
