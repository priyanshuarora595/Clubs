from django.shortcuts import render , redirect
from TechnoClubs.settings import MEDIA_ROOT
from datetime import datetime

# Create your views here.

media_path = str(MEDIA_ROOT)+"/attendance.csv"
media_path_download = str(MEDIA_ROOT)+"\\attendance.csv"

def index(request):
    return render(request, 'index_attendance.html')


def mark_att(request):
    if request.method == "POST":
        with open(media_path,'a') as out_file:
            name = request.POST.get("std_name")
            out_file.write(name)
            out_file.write("\n")
    return render(request, 'index_attendance.html')


def  download(request):
    context={'download_link' : media_path_download}
    return render(request, 'download.html',context)

def download_file(request):
    return redirect("/media/attendance.csv")
