from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import HomeView,CandidateView


urlpatterns = [
    path("",HomeView.as_view(),name="HomeView"),
    path("candidate/<int:pk>",CandidateView.as_view(),name="CandidateView"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)