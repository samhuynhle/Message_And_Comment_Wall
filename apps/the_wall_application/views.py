from django.shortcuts import render, redirect
from .models import *
from apps.login_registration_app.models import *
from time import strftime, strptime
from datetime import date, datetime, timezone

# Create your views here.
def wall(request, user_id):
    if request.session['user_id'] == 'logged out':
        return redirect('/')

    context = {
        'user': User.objects.get(id=user_id),
        'messages': Message.objects.all(),
        'comments': Comment.objects.all(),
    }
    return render(request,'the_wall_application/the_wall_home.html',context)

def post_message(request):
    if request.session['user_id'] == 'logged out':
        return redirect('/')

    current_user = User.objects.get(id=request.POST['user_id'])
    new_message = Message.objects.create(message=request.POST['message'], user=current_user)
    new_message.save()
    
    return redirect(f"/wall/{request.POST['user_id']}")

def post_comment(request):
    if request.session['user_id'] == 'logged out':
        return redirect('/')

    current_user = User.objects.get(id=request.POST['user_id'])
    current_message = Message.objects.get(id=request.POST['message_id'])
    new_comment = Comment.objects.create(comment=request.POST['comment'], user=current_user, message=current_message)
    new_comment.save()
    
    return redirect(f"/wall/{request.POST['user_id']}")

def delete_comment(request):
    if request.session['user_id'] == 'logged out':
        return redirect('/')

    current_comment = Comment.objects.get(id=int(request.POST['comment_id']))
    comment_time = current_comment.created_at

    elapsed_time = calculate_time(comment_time)

    if elapsed_time < 1800:
        current_comment.delete()

    return redirect(f"/wall/{request.POST['user_id']}")

def delete_message(request):
    if request.session['user_id'] == 'logged out':
        return redirect('/')

    current_message = Message.objects.get(id=request.POST['message_id'])
    message_time = current_message.created_at

    elapsed_time = calculate_time(message_time)

    if elapsed_time < 1800:
        current_message.delete()    

    return redirect(f"/wall/{request.POST['user_id']}")

def calculate_time(difference):
    right_now = datetime.now(timezone.utc)
    elapsed_time = right_now - difference
    return elapsed_time.total_seconds()

