from django.shortcuts import render
from django.contrib.auth.models import User
from core.models import MyUser
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required



def index(request):
    user = request.user if request.user.is_authenticated() else None
    content = {
        'active_menu': 'index',
        'user': user,
    }
    return render(request, "core/index.html", content)


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if not user.is_superuser:
                return HttpResponseRedirect(reverse('core:index'))
            else:
                return HttpResponseRedirect(('/admin'))
        else:
            state = 'not_exist_or_password_error'
    content = {
        'state': state,
        'user': None
    }
    return render(request, 'core/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('core:index'))

def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('core:index'))
    state = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create_user(username=username, password=password,
                                                    email=request.POST.get('email', ''))
                new_user.save()
                new_my_user = MyUser(user=new_user, nickname=request.POST.get('nickname', ''))
                new_my_user.save()
                state = 'success'
    content = {
        'state': state,
        'user': None,
    }
    return render(request, 'core/signup.html', content)

@login_required
def set_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'
        else:
            state = 'password_error'
    content = {
        'user': user,
        'state': state,
    }
    return render(request, 'core/set_password.html', content)