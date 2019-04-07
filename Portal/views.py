from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .models import Post, Nominee, Voter

# Create your views here.

def get_nominee_list(user):
    post = Post.objects.get(name=user.stage)
    if post.type == 'General':
        nominees = Nominee.objects.filter(post=post)
    else:
        nominees = Nominee.objects.filter(post=post).filter(house=user.house)
    return nominees

def get_next_stage(user, post):
    if user.house == 'NONE':
        limit = Post.objects.filter(type='General').count()
    else:
        limit = Post.objects.all().count()
    
    if post.id < limit:
        next_stage = Post.objects.get(id=(post.id+1)).name
    else:
        next_stage = 'logout'
    return next_stage

@login_required(login_url='/')
@transaction.atomic
def vote_view(request):
    user = request.user
    if request.method == 'GET':
        if user.stage == 'index':
            user.stage = Post.objects.get(id=1).name
            user.save()
        elif user.stage == 'logout':
            return redirect('/logout')
        nominees = get_nominee_list(user)
        return render(request, 'vote.html', {'nominees': nominees})    
    elif request.method == 'POST':
        if request.POST.get('submit') and request.POST.get('optradio'):
            nominee = Nominee.objects.get(name=request.POST.get('optradio'))
            if user.stage != nominee.post.name:
                print('{} is at {} but tried voting for {}'.format(user.name, user.stage, nominee.name))
                return redirect('/elections')
            error_message = "Your house ({}) doesn't match the nominee's house ({})".format(user.house, nominee.house)
            assert nominee.house == user.house or nominee.house == 'NONE', error_message
            user.stage = get_next_stage(user, nominee.post)
            nominee.votes += 1
            nominee.save()
            user.save()
            return redirect('/elections')
        return redirect('/elections')
        

def thanks_view(request):
    return render(request, 'thanks.html')

