from django.shortcuts import render
from home.models import Feedback
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')
def placement(request):
    return render(request,'placements.html')
def pythond(request):
    return render(request,'pythond.html')
def pythonmt(request):
    return render(request,'pythonmt.html')
def pythonat(request):
    return render(request,'pythonat.html')
def apti(request):
    return render(request,'apti.html')
def verbal(request):
    return render(request,'verbal.html')
def feedback(request):
    if request.method=='POST':
        name=request.POST.get('name')
        pno=request.POST.get('pno')
        email=request.POST.get('email')
        feedback=request.POST.get('feedback')
        feedback=Feedback(name=name,pno=pno,email=email,feedback=feedback,date=datetime.today())
        feedback.save()
    return render(request,'feedback.html')