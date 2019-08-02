from django.db import models


# Create your models here.
class album(models.Model):
    album_title=models.CharField(max_length=250)
    artist=models.CharField(max_length=250)
    genre=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=1000)
    def __str__(self):
        return self.album_title +" by "+ self.artist

class song(models.Model):
    album=models.ForeignKey(album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    title=models.CharField(max_length=250)
    is_favurite=models.BooleanField(default=False)
    def __str__(self):
        return self.title
        