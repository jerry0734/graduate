from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from .forms import BlogUserCreationForm
from .models import allUser


# Create your views here.
def user_login(request):
    """用户登录"""
    error = ''
    redirect_field_name = REDIRECT_FIELD_NAME
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('blog:index'))
            else:
                error = '您的账号已被停用，请联系<a href="mailto:admin@hellojerry.cn">管理员</a>'
        else:
            error = '请检查您的用户名或者密码是否正确！'
            print('Wrong account: {0},{1}'.format(username, password))

    context = {'error': error}
    return render(request, 'myuser/login.html', context)


# 限制修饰符
@login_required
def user_logout(request):
    """用户注销"""
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def user_register(request):
    """用户注册"""
    errors = []
    # if request.method == "POST":
    if request.method != "POST":
        form = BlogUserCreationForm()
    else:
        form = BlogUserCreationForm(data=request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password2', '')
        if form.is_valid():
            user = form.save()
            authenticated_user = authenticate(username=username, password=password)
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('blog:index'))
        else:
            for key, value in form.errors.items():
                errors.append(value.as_text)

    context = {'form': form, 'errors': errors}
    return render(request, 'myuser/register.html', context)
