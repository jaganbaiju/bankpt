from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Data,Branch
from .forms import DataCreationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        try:
            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already exist')
                    return redirect('register')

                else:
                    user = User.objects.create_user(username=username, password=password)
                    user.save()

                    return redirect('login')

            else:
                messages.info(request,'Password is not matching')
                return redirect('register')

        except:
            return redirect('register')

        return redirect('/')

    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('person_add')

        else:
            messages.info(request,'Incorrect entry')
            return redirect('login')



    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def data_create_view(request):
    form = DataCreationForm()
    if request.method == 'POST':
        # if request.method == 'POST':
        #     name = request.POST['name']
        #     dob = request.POST['dob']
        #     age = request.POST['age']
        #     gender = request.POST['gender']
        #     phone = request.POST['phone']
        #     mail = request.POST['mail']
        #     address = request.POST['address']
        #     account = request.POST['account']
        #     material = request.POST.getlist('material')
        #
        #     data = Data(name=name, dob=dob, age=age, gender=gender, phone=phone, mail=mail, address=address,
        #                 account=account, material=material)
        #     data.save()
        form = DataCreationForm(request.POST)
        if form.is_valid():
            form.save()


            messages.info(request, 'Application Accepted')
            return render(request,'page.html')
        else:
            messages.info(request, 'Application Not Accepted')
            return render(request,'page.html')
    return render(request, 'login_page.html', {'form': form})


# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'abc.html', {'branches': branches})
