from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from .modelForm import VideoForm


def upload_file(request):


    if request.method == 'POST':
        upload = request.FILES['video']
        print(upload.name)
        print(upload.size)
    #    if form.is_valid():
    #        # file is saved
    #        form.save()
    #        return HttpResponseRedirect('/success/url/')
    #else:
    #    form = VideoForm()
    return render(request, 'videoUpload/fileUpload.html')


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
