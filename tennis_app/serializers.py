from rest_framework import serializers
from .models import Signup, PlayerRanking, UploadImages, UploadTournamentVideos, UploadHighlightVideos, UploadTeamVideos, LatestNews, Results

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ('id', 'fname', 'lname', 'dob', 'email', 'password', 'nationality', 'handbat', "imageurl", "currenteam", "lastchamp", "datelastchamp", "locatelastchamp", "favoriteplayer", "points")

class PlayerRankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerRanking
        fields = ('id', 'firstname', 'leaguetype', 'points')

class UploadImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImages
        fields = ("id", "title", "imageurl")

class UploadTournamentVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadTournamentVideos
        fields = ("id", "videodescription" ,"videourl")

class UploadHighlightVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadHighlightVideos
        fields = ("id", "videodescription" ,"videourl")

class UploadTeamVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadTeamVideos
        fields = ("id", "videodescription" ,"videourl")

class LatestNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestNews
        fields = ("id", "title" ,"description", "image")  

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = ("id", "player1" ,"player1_first_set_score", "player1_second_set_score", "player1_third_set_score", "player2", "player2_first_set_score", "player2_second_set_score", "player2_third_set_score", "result_type")  

