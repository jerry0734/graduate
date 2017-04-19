from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['author_name', 'email', 'content']
        # 渲染到表单上的标签，空的表示不生成
        labels = {'content': ""}
        widgets = {'content': forms.Textarea(attrs={'rows': 3})}
