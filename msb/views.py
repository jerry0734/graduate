from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Message
from .forms import MessageForm


# Create your views here.

def MessageBoard(request):
    if request.method != "POST":
        form = MessageForm()
    else:
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('msb:board'))

    messages = Message.objects.all().order_by('-published_time')

    context = {'form': form, 'messages': messages}
    return render(request, 'msb/board.html', context)


def msb_manage(request):
    """管理留言板"""
    pass
