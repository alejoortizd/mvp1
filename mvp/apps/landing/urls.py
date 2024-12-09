from django.urls import path

from mvp.apps.landing.views import LandingView

urlpatterns = [
    path("", LandingView.as_view(), name="landing"),
]
