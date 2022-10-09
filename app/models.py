from django.db import models


# Create your models here.

# class TorrentDetails(models.Model):
#     title = models.CharField(max_length=1000)
#     webLink = models.CharField(max_length=1000)
#     magnetLink = models.CharField(max_length=2000, null=True)
#     size = models.IntegerField(null=True)
#
#     def __str__(self):
#         return self.title

class Link(models.Model):
    m_link = models.CharField(max_length=2000)

    def __str__(self):
        return self.m_link


class FileLink(models.Model):
    f_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.f_link


