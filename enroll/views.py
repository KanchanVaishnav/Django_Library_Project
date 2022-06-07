from pyexpat.errors import messages
from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import BookForm
from enroll.models import Book
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


#This function used to add book and show all books in database
def add_show(request):
    if request.method=="POST":
        bm=BookForm(request.POST)
        if bm.is_valid():
            bm.save()
        bm=BookForm()
    else:
        bm=BookForm()
    stud = Book.objects.all()
    return render(request,'enroll/Add&Show.html',{'form':bm,'stu':stud})

def update_data(request,id):
    if request.method=="POST":
        pi=Book.objects.get(pk=id)
        bm=BookForm(request.POST, instance=pi)
        if bm.is_valid():
            bm.save()
    else:
        pi=Book.objects.get(pk=id)
        bm=BookForm(instance=pi)
    return render(request,'enroll/update.html', {'form':bm})


#This function used to delete book
def delete_data(request,id):
    if request.method=="POST":
        pi = Book.objects.get(id=id)
        pi.delete()
    return HttpResponseRedirect('/')

def admin_login(request):
    if request.method=="POST":
        bm=AuthenticationForm(request=request, data=request.POST)
        if bm.is_valid():
            uname=bm.cleaned_data['username']
            upass=bm.cleaned_data['password']
            user=authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('home/')
    else:
        bm=AuthenticationForm()
    return render(request,'enroll/login.html', {'form':bm}) 

def admin_logout(request):
    logout(request)
    print("Yor are logout from system")
    return HttpResponseRedirect('/')