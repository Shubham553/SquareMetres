from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
# from django.contrib.auth.models import User
# from enquiries.models import Enquiry
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import *


def register(request):
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES)
        email = request.POST['email']
        print(email)
        if UserProfile.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('register/')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'user registered succesfully')
            return redirect('/')
    else:
        form = UsersForm()
    return render(request, 'sign_up.html', {'form': form})


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            login(request, user)
            messages.success(request, 'user login succesfully')
            return redirect('/')

        else:
            messages.error(request, 'Incorrect Username/Password')

    return render(request, 'login.html')


def userlogout(request):
    logout(request)
    messages.success(request, 'user logout succesfully')
    return redirect('/')


# def dashboard(request):
#     user_enquiries = Enquiry.objects.order_by('-enquiry_date').filter(user_id=request.user.id)
#     context = {
#         'user_enquiries': user_enquiries
#     }
#     return render(request, 'useraccounts/dashboard.html', context)

class Dashboard(DetailView):
    template_name = 'dashboard.html'
    queryset = UserProfile.objects.all()
