from django.shortcuts import render
from django.views import View


class LandingView(View):
    def get(self, request):
        context = {}
        return render(request, "landing.html", context=context)
