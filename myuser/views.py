from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from .forms import BlogUserCreationForm, ProfileForm, PrivateForm
from .models import allUser
from blog_articles.models import Comments


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


def profile(request, user_id):
    user = allUser.objects.get(id=user_id)
    comments = Comments.objects.filter(user=user_id).order_by('-published_time')
    form = ProfileForm()
    context = {'myuser': user, 'comments': comments, 'form': form}
    return render(request, 'myuser/profile.html', context)


@login_required
def change_avatar(request, user_id):
    error = None
    if request.method != 'POST':
        form = ProfileForm()
    else:
        user = allUser.objects.get(id=user_id)
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('account:profile', args=[user_id]))
        else:
            error = '您上传的头像出了问题了'
            return HttpResponseRedirect(reverse('account:profile', args=[user_id]))


@login_required
def userlist(request):
    user_list = allUser.objects.all()
    context = {
        'user_list': user_list
    }
    return render(request, 'myuser/userlist.html', context)


@login_required
def disabled_user(request, user_id):
    """禁用账户"""
    user = allUser.objects.get(id=user_id)
    if user.is_superuser == False:
        user.is_active = False
        user.save()
    else:
        return redirect('account:userlist')
    return redirect('account:userlist')


@login_required()
def abled_user(request, user_id):
    """启用账户"""
    user = allUser.objects.get(id=user_id)
    user.is_active = True
    user.save()
    return redirect('account:userlist')

# @login_required
# def send_messages(request, receiver_id):
#     form = PrivateForm()
#     receiver = allUser.objects.get(id=receiver_id)
#     user = request.user
#     if request.method != "POST":
#         form = PrivateForm()
#     else:
#         form = PrivateForm(data=request.POST)
#         form.save(commit=False)
#         form.sender = request.user
#         form.recevier = receiver_id
#         form.save(commit=True)
#         return redirect(to='blog:index')
#     context = {
#         'receiver': receiver,
#         'form': form,
#     }
#     return render(request, 'myuser/post_private.html', context)
#
#
# def message_user(request, receiver):
#     pass


# def message_list(request, sender, receiver):
#     pass
