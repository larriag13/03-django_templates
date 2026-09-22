from urllib import request

from django.shortcuts import render

# Create your views here.
def p1(request):
    data={"nombre":"Benjamín","apellido":"Sanhueza", "edad": 19}
    return render(request, 'perfil/v1.html', data)

def p2(request):
    data={"nombre":"Benjamín","apellido":"Sanhueza", "edad": 19}
    return render(request, 'perfil/v2.html', data)