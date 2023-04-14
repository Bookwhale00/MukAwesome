from django.shortcuts import render, redirect
from .models import PostingModel, UserInfo
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def home_view(request):
    all_posting = PostingModel.objects.all().order_by('-created_at')
    return render(request, 'posting/home.html', {'all_posting': all_posting})


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
        title = request.POST.get('title', '')
        thumbnail = request.POST.get('thumbnail', '')
        content = request.POST.get('content', '')

        if title == '':
            return render(request, 'posting/posting.html')
        elif content == '':
            return render(request, 'posting/posting.html')
        else:
            posting_ = PostingModel.objects.create(author=author, title=title, thumbnail=thumbnail, content=content)
            return redirect('/api/posting-detail/' + str(posting_.id))

def posting_detail_view(request, id):
    if request.method == 'GET':
        select_posting = PostingModel.objects.get(id=id)
        default_thumbnail = 'https://velog.velcdn.com/images/e_elin/post/393c51bc-9fef-48a8-ae11-f47bb3e57bbc/image.png'

        if select_posting.thumbnail == '':
            select_posting.thumbnail = default_thumbnail

        return render(request, 'posting/posting_detail.html', {'select_posting': select_posting})

@login_required
def mypage_list_view(request, username):
    if request.method == 'GET':
        author_wanted = UserInfo.objects.get(username=username)
        my_posting = PostingModel.objects.filter(author=author_wanted).order_by('-created_at')
        return render(request, 'posting/mypage.html', {'my_posting': my_posting})


@login_required
def mypage_edit_view(request,pk):
    posting_edit = PostingModel.objects.get(id=pk)
    if request.method == "POST":
        title = request.POST.get("title_edit","")
        thumbnail = request.POST.get("thumbnail_edit","")
        content = request.POST.get("content_edit","")
        if title == '': # 수정
            return render(request, 'posting/edit.html', {'error': '제목을 작성해주세요!'})
        elif content == '':
            return render(request, 'posting/edit.html', {'error': '내용을 작성해주세요!'})
        else:
            posting_edit.title = title
            posting_edit.thumbnail = thumbnail
            posting_edit.content = content
            posting_edit.save()
            return redirect('/api/posting-detail/'+str(posting_edit.pk))

    elif request.method == "GET":
        user = request.user.is_authenticated
        if user:
            return render(request, 'posting/edit.html', {'posting_edit': posting_edit})
        else:
            return render(request, 'user/signin.html')

def mypage_delete_view(request, pk):
    posting_delete = PostingModel.objects.get(id=pk)
    if request.user.is_authenticated and request.user == posting_delete.author:
        posting_delete.delete()
        return redirect('/api/mypage/'+ str(request.user.username))
    else:
        return redirect('/api/posting-detail/' + str(pk))