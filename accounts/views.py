from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'accounts/home.html') 

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/account')

    else:
        form = RegistrationForm()
        
    args = {'form': form}
    return render(request, 'accounts/register.html', args)

@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
        if request.method == 'POST':
                form = UserChangeForm(request.POST, instance=request.user)

                if form.is_valid():
                        form.save()
                        return redirect('/account/profile')
        else:
                form = UserChangeForm(instance=request.user)

        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def view_program(request):
    return render(request, 'accounts/program.html') 


def view_contact(request):

    if request.method == 'POST':
        subject = request.POST.get("subject")        
        from_email = request.POST.get("from_email")
        message = request.POST.get("message")

        send_mail(subject, message, from_email, ['info@gwdconcept.com.ng'])
    return render(request, 'accounts/contact.html')

