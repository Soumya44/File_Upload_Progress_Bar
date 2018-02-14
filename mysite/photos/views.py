import time

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View

from .forms import PhotoForm
from .models import Photo
from django.http import HttpResponseRedirect

class ProgressBarUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'photos/progress_bar_upload/index.html', {'photos': photos_list})

    def post(self, request):
        time.sleep(1)  # Not Needed
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

def index(request):
    photos_list = Photo.objects.all()
    return render(request, 'photos/progress_bar_upload/index.html', {'photos': photos_list})


def clear_database(request):
    Photo.objects.all().delete()
    return redirect(request.POST.get('next'))
