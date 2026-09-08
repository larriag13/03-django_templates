from django.shortcuts import render

# Create your views here.
def v1(request):
    return render(request, "Benjamín/v1.html")

def v2(request):
    return render(request, "Benjamín/v2.html")