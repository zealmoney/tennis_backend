from django.shortcuts import render
from rest_framework import viewsets
from .models import Signup, PlayerRanking, UploadImages, UploadTournamentVideos, UploadHighlightVideos, UploadTeamVideos, LatestNews, Results
from .serializers import SignupSerializer, PlayerRankingSerializer, UploadImagesSerializer, UploadTournamentVideosSerializer, UploadHighlightVideosSerializer, UploadTeamVideosSerializer, LatestNewsSerializer, ResultSerializer

class SignupView(viewsets.ModelViewSet):
    queryset = Signup.objects.all().order_by("-points")
    serializer_class = SignupSerializer

class PlayerRankingView(viewsets.ModelViewSet):
    queryset = PlayerRanking.objects.all().order_by("-points")
    serializer_class = PlayerRankingSerializer

class UploadImagesView(viewsets.ModelViewSet):
    queryset = UploadImages.objects.all()
    serializer_class = UploadImagesSerializer

class UploadTournamentVideoView(viewsets.ModelViewSet):
    queryset = UploadTournamentVideos.objects.all()
    serializer_class = UploadTournamentVideosSerializer

class UploadHighlightVideoView(viewsets.ModelViewSet):
    queryset = UploadHighlightVideos.objects.all()
    serializer_class = UploadHighlightVideosSerializer

class UploadTeamVideoView(viewsets.ModelViewSet):
    queryset = UploadTeamVideos.objects.all()
    serializer_class = UploadTeamVideosSerializer

class LatestNewsView(viewsets.ModelViewSet):
    queryset = LatestNews.objects.all()
    serializer_class = LatestNewsSerializer

class ResultView(viewsets.ModelViewSet):
    queryset = Results.objects.all()
    serializer_class = ResultSerializer



