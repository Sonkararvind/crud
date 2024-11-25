from django.shortcuts import render

# Create your views here.
def INDEX(request):
    return render(request,'index.html')