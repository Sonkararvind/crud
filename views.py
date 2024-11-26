from django.shortcuts import render
from crud_app.models import Employees
# Create your views here.
def INDEX(request):
    emp=Employees.objects.all()

    context={
        'emp':emp,
    }
    return render(request,'index.html',context)

def ADD(request):
 if request.method=='POST':
     Name=request.POST.get('name')
     Email=request.POST.get('Email')
     Address=request.POST.get('Address')
     Phone=request.POST.get('phone')
     
    
 emp=Employees(
       name = name,
      email = email,
      address = address,
     phone = phone

  )

 emp.save()
 return redirect('home')

 return render(request,'add.html')
