from django.shortcuts import render
from matplotlib.style import context
from rest_framework.views import APIView
from .models import Feed

# Create your views here.
class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # 피드에 있는 모든 data를 가져옴 , select *from content_feed;와 동일

        return render(request, "instagram/main.html", context=dict(feeds=feed_list))