from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import InterviewModel
from .forms import InterviewForm


class InterviewView(View):
    template_name = 'add_interview.html'

    def get(self, request):
        interviews = InterviewModel.objects.all()
        form = InterviewForm()
        return render(request, self.template_name, {'interviews': interviews, 'form': form})

    def post(self, request):
        form = InterviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required(login_url='login'), name='dispatch')
class HomeView(View):
    template_name = "home.html"

    def get(self, request):
        return render(request, self.template_name)
    

class SignUpView(View):
    template_name = 'signup.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})
    

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login') 
