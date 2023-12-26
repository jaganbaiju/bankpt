from django.shortcuts import render
from .models import MainDetails,Faclities

# Create your views here.
def Home(request):
    obj=MainDetails.objects.all()
    obb=Faclities.objects.all()
    return render(request,'index.html',{'obj':obj,'obb':obb})


