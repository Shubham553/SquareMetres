from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
# from django.contrib.auth.models import User
from enquiries.models import Enquiry
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView
from catalogue.models import Catalogue
from django.contrib.messages.views import SuccessMessageMixin
from .forms import *


def register(request):
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES)
        # email = request.POST['email']
        # print(email)
        # if UserProfile.objects.filter(email=email).exists():
        #     messages.error(request, 'email already exists')
        #     return redirect('register/')
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, 'user registered succesfully')
            else:
                messages.error(request, 'unable to authenticate')
            return redirect('/profiles/userlogin')
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
            pk = user.pk
            if user.is_dealer:
                return redirect('/profiles/dashboard/' + str(pk))
            else:
                return redirect('/')
            messages.success(request, 'user login successfully')
            return redirect('/')

        else:
            messages.error(request, 'Incorrect Username/Password')

    return render(request, 'login.html')


def userlogout(request):
    logout(request)
    messages.success(request, 'user logout succesfully')
    return redirect('/')


class Dashboard(DetailView):
    template_name = 'dashboard.html'

    def get_queryset(self):
        return UserProfile.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        # properties = Catalogue.objects.all(pk=self.request.user.pk)
        user_data = UserProfile.objects.get(pk=self.kwargs['pk'])
        print(user_data)
        # properties = user_data.profile.all()
        property = Enquiry.objects.order_by('-enquiry_date').filter(buyer_id=self.request.user.id)
        # print(user, properties, property)
        context.update({
            'user': user_data,
            # 'properties': properties,
            'property': property
        })
        return context


class UserUpdate(UpdateView, SuccessMessageMixin):
    success_message = 'Update sucessfully'
    template_name = 'update_user.html'
    form_class = UserUpdateForm
    success_url = '/'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(UserProfile, id=pk)
