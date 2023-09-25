from django.db import models
from cloudinary.models import CloudinaryField

class Signup (models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    dob =   models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, default="")
    nationality = models.CharField(max_length=255, default="")
    handbat = models.CharField(max_length=255, default="")
    imageurl = models.TextField(default="")
    currenteam = models.TextField(default="")
    lastchamp = models.TextField(default="")
    datelastchamp = models.DateField(default="2023-01-01")
    locatelastchamp = models.TextField(default="")
    favoriteplayer = models.TextField(default="")
    points = models.IntegerField(default = "0")
    

    def __str__(self):
        return self.fname
    
class PlayerRanking(models.Model):
    firstname = models.ForeignKey(Signup, on_delete=models.CASCADE)
    leaguetype = models.CharField(max_length=255, default="")
    points = models.IntegerField()

class UploadImages(models.Model):
    title =  models.TextField()
    imageurl = CloudinaryField("image")

class UploadTournamentVideos(models.Model):
    videodescription = models.TextField()
    videourl = models.TextField()

class UploadHighlightVideos(models.Model):
    videodescription = models.TextField()
    videourl = models.TextField()

class UploadTeamVideos(models.Model):
    videodescription = models.TextField()
    videourl = models.TextField()

class LatestNews(models.Model):
    title = models.TextField()
    description = models.TextField()
    image = CloudinaryField("image")

class Results(models.Model):
    player1 = models.CharField(max_length=255)
    player1_first_set_score = models.IntegerField(default=0)
    player1_second_set_score = models.IntegerField(default=0)
    player1_third_set_score = models.IntegerField(default=0)

    player2 = models.CharField(max_length=255)
    player2_first_set_score = models.IntegerField(default=0)
    player2_second_set_score = models.IntegerField(default=0)
    player2_third_set_score = models.IntegerField(default=0)

    RANKING_WEEK1 = '1'
    LEAGUE_WEEK2 = '2'
    LEAGUE_WEEK3 = '3'
    LEAGUE_WEEK4 = '4'
    SUPER4 = '5'

    RANKINGS = [
        (RANKING_WEEK1, 'Ranking Week 1'),
        (LEAGUE_WEEK2, 'League Week 2'),
        (LEAGUE_WEEK3, 'League Week 3'),
        (LEAGUE_WEEK4, 'League Week 4'),
        (SUPER4, 'Super 4')
    ]

    result_type = models.CharField(max_length=10, choices=RANKINGS, default=RANKING_WEEK1)

    


    


