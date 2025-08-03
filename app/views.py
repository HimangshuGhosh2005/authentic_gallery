from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import database


# Create your views here.
def gallery(req):
    if req.user.id is None or req.user.is_superuser: 
              return  redirect("loginpage")
    if req.method=="POST":
        if "upload" in req.POST:
            files=req.FILES.getlist('file')
            
            for file in files:
                data=database(name=req.user.username,images=file)
                data.save()
            return render(req,'gallery.html',{'user':req.user.username,'message':"file uploaded successfully!"})
        if "view" in req.POST:
            print("entering viewgallery")
            display=database.objects.filter(name=req.user.username)
            return render(req,'gallery.html',{'user':req.user.username,'imagefile':display})
    return render(req,'gallery.html',{'user':req.user.username})
          




def logingin(req):
    if req.method=="POST":
        username=req.POST.get("username")
        password=req.POST.get("password")
        user=authenticate(req,username=username,password=password)
        if  user  :
           login(req,user)
           return redirect("gallery")
        else:
             return render(req,'loging.html',{"message":"invalid credentials"})
                
    return render(req,'loging.html')

def signup(req):
     if req.method=="POST":
          username=req.POST.get("username")
          password=req.POST.get("password")
          if not User.objects.filter(username=username).exists():
           user=User.objects.create_user(username=username,password=password)
           user.save()
           if user.is_authenticated:
               login(req,user)
               return redirect("gallery")
          else:
             return render(req,'signup.html',{'message':'User already exists'})     
          
     return render(req,"signup.html")

def logouting(req):
    logout(req)
    return redirect("loginpage")

def delimg(req):
    img=database.objects.get(id=list(req.POST)[-1])
    img.delete()
    return redirect("gallery")

def view(req):
 obj=database.objects.get(id=list(req.POST)[-1])
 return render(req,'view.html',{"img":obj})