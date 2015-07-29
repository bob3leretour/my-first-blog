from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post,Category, Main_category
from .forms import PostForm, LoginForm, RegisterForm, ContactForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Count

def post_contact(request):
    if request.method == 'POST':
        sender = request.POST['sender']
        subject = request.POST['subject']
        message = request.POST['message']
        result = send_mail(subject, message,sender,['benjaminchomel@hotmail.com'], fail_silently=False)

        if  result == 1 :
           return HttpResponse("Sent successfully")
        else:

            return HttpResponse("Sending email failed")

    else:
        form = ContactForm()
        return render(request, 'blog/post_contact.html', {'form': form})

def post_list(request, cat):
    #post = get_object_or_404(Post, pk=pk)
    main_category = get_object_or_404(Main_category, pk=cat)
    post1 = Post.objects.filter(main_category = main_category)
    posts = post1.filter(published_date__lte=timezone.now()).order_by('-published_date')
    categories = Category.objects.all()
    for cat in categories:
        if len(posts.filter(category=cat))== 0 :
            categories = categories.exclude(name=cat.name)

    return render(request, 'blog/post_list.html', {'posts': posts, 'categories':categories})




def post_main(request):
    posts = Post.objects.filter(for_mainpagedisplay=True).order_by('-published_date')
    return render(request, 'blog/post_main.html', {'posts': posts})

def post_details(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'post': post})

@login_required(login_url='/post/login')
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required(login_url='/post/login')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required(login_url='/post/login')
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    form = PostForm(instance=post)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if  user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'blog/logged.html', {})
            else:
                return HttpResponse("Your  account is disabled.")
        else:

            return HttpResponse("Invalid login details supplied.")

    else:
        form = LoginForm()
        return render(request, 'blog/post_login.html', {'form': form})


def post_logout(request):
    logout(request)
    #redirect('blog.views.post_list',)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if(password == password2 and password != '' and password2 != '') :
            user = User.objects.create_user(username, password = password)
        else :
            form = RegisterForm()
            return render(request, 'blog/post_register.html', {'form': form})

        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
        return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        form = RegisterForm()
        return render(request, 'blog/post_register.html', {'form': form})

