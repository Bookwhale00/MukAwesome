from django.shortcuts import render, redirect
from .models import PostingModel,UserInfo
from django.contrib.auth.decorators import login_required



def home_view(request):

        return render(request, 'posting/home.html')

def posting_view(request):
    if request.method == 'GET':

        return render(request, 'posting/posting.html')

    elif request.method =='POST':
        user = request.user

        author = user
        title = request.POST.get('title','')
        thumbnail = request.POST.get('thumbnail','')
        content = request.POST.get('content','')

        if title == '':
            return render(request, 'posting/posting.html', {'error': '제목을 작성해주세요!'})
        elif content == '':
            return render(request, 'posting/posting.html', {'error': '내용을 작성해주세요!'})
        else:
            PostingModel.objects.create(author=author,title=title,thumbnail=thumbnail, content=content)
            return redirect('/api/posting-detail/<int:id>')



def posting_detail_view(request,id):
    if request.method == 'GET':
        select_posting = PostingModel.objects.get(id=id)
        return render(request, 'posting/posting_detail.html',{'select_posting':select_posting})

    elif request.method == 'POST':

        return redirect('/api/posting-detail/<int:id>')

def mypage_view(request):
    if request.method == 'GET':

        # return redirect('/api/mypage/<str:username>')

        return render(request, 'posting/mypage.html')


