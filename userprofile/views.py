from django.shortcuts import render, redirect


from django.contrib.auth import authenticate, login ,password_validation,hashers
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from fileapp.views import create_serializer
from fileapp.models import FilesData
from django.contrib.auth import logout

def login_page(request):
	if request.user.is_authenticated :
		return redirect('home')
	if request.method=='POST':
		name = request.POST.get("username")
		passo = request.POST.get("password")
		user = authenticate(request ,username=name, password=passo)
		if user is not None:
       		 login(request, user)
       		 return redirect('home')
	return render(request ,"login.html")


def logout_view(request):
    logout(request)
    return redirect('login')	

def register_page(request):
	if request.method=='POST':
		new_user = User()
		new_user.username = request.POST.get('first_name')
		new_user.password =  hashers.make_password( request.POST.get('password'),salt=None, hasher='default')
		new_user.save()
		login(request, new_user)
		return redirect('home')	
	return render(request , "register.html")


@login_required(login_url='/login')
def home_page(request):
	data = FilesData.objects.all()
	content = {"data":data}
	return render(request , "home.html",content)

@login_required(login_url='/login')
def profile_page(request,idx):
	files = FilesData.objects.filter(user=request.user)
	content = create_serializer(files)
	return render(request , "profile.html" ,content )
	

def validate_username(request):
    username = request.GET.get('username')
    data = {
        'is_taken': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)


def validate_pass(request):
	password = request.GET.get('password')
	try :
		a = password_validation.validate_password(password)
	except:
		a = 'False'
	data = {'valid' : a	}
	return JsonResponse(data)


