from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import BlogUserCreationForm
from .models import allUser


# Create your views here.
def user_login(request):
    """用户登录"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('blog:index'))
            else:
                return HttpResponse("您的账号已被停用，请联系管理员")
        else:
            print('Wrong account: {0},{1}'.format(username, password))
            return HttpResponse("请检查您的用户名或者密码是否正确！")
    else:
        return render(request, 'myuser/login.html', {})


# 限制修饰符
@login_required
def user_logout(request):
    """用户注销"""
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))


def register(request):
    # if request.method == "POST":
    if request.method != "POST":
        form = BlogUserCreationForm()
    else:
        form = BlogUserCreationForm(data=request.POST)
