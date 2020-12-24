from django import forms

class CommentForm(forms.Form):
    id = -1
    comment = forms.CharField(max_length=200, label="Комментарий")

class AddForm(forms.Form):
    title = forms.CharField(max_length=200, label="Заголовок поста")
    text = forms.CharField(max_length=300, label="Текст поста", widget=forms.Textarea(attrs={'class': "col"}))