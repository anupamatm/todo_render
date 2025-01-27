from pyexpat.errors import messages
from django.shortcuts import render,redirect

from user.models import User

# Create your views here.


def index(request):
    return render(request, 'user/index.html')

def home(request):
    return render(request, 'user/user_home.html')

def login(request):
    msg=''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = User.objects.get( email=username, password=password)        
        if user is not None:            
            return redirect('user:home')
        else:
            msg='Invalid username or password!'
    return render(request, 'user/login.html',{'status':msg})


def signup(request):
    msg=""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            msg="Email already exists!"           
            return render(request, 'user/signup.html',{'status':msg})
        
        # Create a new user
        user = User(name=name, email=email,mobile=mobile, password=password)        
        user.save()
        msg="Your account has been created successfully!"  

    return render(request, 'user/signup.html',{'status':msg})