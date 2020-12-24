from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment, User
from .forms import CommentForm, AddForm
from django.views.generic.base import View
from django.contrib.auth import logout, login
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



def forum(request):
    posts = Post.objects.all() 
    commform = CommentForm()
    if 'post' in request.POST:
        if(request.user.id is not None):
            print(request.user.id)
        post_id = request.POST['post']
        comment_post = Post.objects.filter(id=post_id).first()
        comment_text = request.POST['comment']
        print(request.POST)
        new_comment = Comment.objects.create(text=comment_text, user=User(request.user.id), order=3, post_id=post_id)
        comment_post.comments.add(new_comment)
        new_comment.save()
        comment_post.save()
        cleanform = CommentForm()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'forum.html', { 'posts':posts, 'commentform':commform })


class RegisterFormView(FormView):
    form_class = UserCreationForm
    #form_class.

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "login"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):

    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")

def add_post(request):
    add_form = AddForm()
    return render(request, 'add_post.html', { 'add_form':add_form })

def add(request):
    add_form = AddForm()
    posts = Post.objects.all() 
    commform = CommentForm()
    if 'title' in request.POST:
        r_title = request.POST['title']
        r_text = request.POST['text']
        author = User.objects.filter(id=request.user.id).first()
        print(request.POST)
        new_post = Post.objects.create(title=r_title, message=r_text, username=author)
        new_post.save()
        return HttpResponseRedirect('/')
        #return render(request, 'forum.html', { 'posts':posts, 'commentform':commform })
    else:
        return HttpResponseRedirect('/')
