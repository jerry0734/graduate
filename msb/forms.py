from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    email = forms.EmailField()

    author_name = forms.CharField(max_length=20)

    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))

    class Meta:
        model = Message
        fields = ['author_name', 'email', 'content']
        # 渲染到表单上的标签，空的表示不生成
        labels = {'content': ""}
