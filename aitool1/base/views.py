from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import UserForm
from .utils import generate_answer,generate_content,generate_questions,evaluate_answer 
# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # pk = request.user.id
    # education = User.objects.get(id=pk)
    # education_level=education.education_level
    content = "Welcome human please enter topic below to get started"
    context = {'content':content}
    return render(request, 'base/home.html',context)

@login_required(login_url='home')
def Content(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    pk = request.user.id
    education = User.objects.get(id=pk)
    education_level = education.education_level
    content = generate_content(q, education_level)
    
    
    # Store 'q' and 'content' in session data
    request.session['q'] = q
    request.session['content'] = content
    
    return render(request, 'base/content.html', {'content': content})
@login_required(login_url='home')
def Question(request):
    # Retrieve 'q' and 'content' from session data
    q = request.session.get('q', '')
    content = request.session.get('content', '')
    
    pk = request.user.id
    education = User.objects.get(id=pk)
    education_level = education.education_level
    question = generate_questions(q,content,education_level)
    
    return render(request, 'base/question.html', {'question': question})

@login_required(login_url='home')
def Evaluation(request):
    # Retrieve 'question' from session data
    question = request.session.get('question', '')
    
    user_answer = request.GET.get('answer') if request.GET.get('answer') is not None else ''
    pk = request.user.id
    education = User.objects.get(id=pk)
    education_level = education.education_level
    corr_answer = generate_answer(question)
    evaluation = evaluate_answer(user_answer,question)
    
    return render(request, 'base/evaluation.html', {'evaluation': evaluation})

def help(request):
    name = request.user.name
    return render(request,'base/help.html',{'name':name})