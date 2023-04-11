from django.shortcuts import render, redirect
from .models import PostingModel
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required




def home_view(request):

        return render(request, 'posting/home.html')

def posting_view(request): # 트윗 안에 홈.에이치티엠엘을 보여주는 함수
    if request.method == 'GET':

        return render(request, 'posting/posting.html')

    elif request.method =='POST':

        return ''

@login_required
def mypage_list_view(request, id):
    if request.method == 'GET':
        user = request.user
        if id == user.id:
            my_posting = PostingModel.objects.filter(author_id=id).order_by('-created_at')
            return render(request, 'posting/mypage.html', {'my_posting': my_posting})
        else:
            return redirect('/')

