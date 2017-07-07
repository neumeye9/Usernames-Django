from django.shortcuts import render, redirect
from models import Usernames
from django.contrib import messages
# Create your views here.

def index(request):
    usernames = Usernames.usernamesManager.all()
    context = {
        "usernames" : usernames
    }
    return render(request, 'usernames_app/index.html', context)

def validate(request):

    check = Usernames.usernamesManager.add(request.POST['username'])

    if check[0] == False:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message) 
            print "Invalid Username"
            return redirect('/')
    else:
        return redirect('/success')

def success(request):
    messages.add_message(request, messages.SUCCESS, "Your username was accepted!")

    usernames = Usernames.usernamesManager.all()
    context = {
        "usernames": usernames
    }
    return render(request, 'usernames_app/success.html', context)

def delete(request, id):
    this = Usernames.usernamesManager.get(id=id)
    this.delete()
    return redirect('/success')
 