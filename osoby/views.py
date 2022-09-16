from django.http import HttpResponse

def index(request):
    return HttpResponse("Witaj w Django! znajde twoja rodzinę")
def info(request):
    return HttpResponse("<p>dane wywiadowcze</p>")

