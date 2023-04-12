from django.shortcuts import render, redirect
from .models import PostingModel
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse




def home_view(request):

        return render(request, 'posting/home.html')


def posting_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return render(request, 'posting/posting.html')
        else:
            return redirect('/api/sign-in')

    elif request.method == 'POST':
            posting_user = request.user
            author = posting_user
            title = request.POST.get('title','')
            thumbnail = request.POST.get('thumbnail','')
            content = request.POST.get('content','')

            if title == '':
                return render(request, 'posting/posting.html', {'error': '제목을 작성해주세요!'})
            elif content == '':
                return render(request, 'posting/posting.html', {'error': '내용을 작성해주세요!'})
            else:
                posting_ = PostingModel.objects.create(author=author,title=title,thumbnail=thumbnail,content=content)

                return redirect('/api/posting-detail/'+str(posting_.id))




@login_required
def posting_detail_view(request, id):
    clicked_posting = PostingModel.objects.get(id=id)
    return render(request, 'posting/posting_detail.html', {'select_posting': clicked_posting})


@login_required
def mypage_list_view(request, id):
    if request.method == 'GET':
        user = request.user
        if id == user.id:
            my_posting = PostingModel.objects.filter(author_id=id).order_by('-created_at')
            return render(request, 'posting/mypage.html', {'my_posting': my_posting})
        else:
            return redirect('/')

