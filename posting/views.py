from django.shortcuts import render, redirect
from .models import PostingModel,UserInfo
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
                PostingModel.objects.create(author=author,title=title,thumbnail=thumbnail, content=content)

                save_posting = PostingModel.objects.get(id=id)
                current_posting = save_posting.id

                return redirect('/api/posting-detail/'+str(current_posting))




def posting_detail_view(request,id):
    if request.method == 'GET':
        select_posting = PostingModel.objects.get(id=id)

        return render(request, 'posting/posting_detail.html', {'select_posting': select_posting})


    elif request.method == 'POST':

        return redirect('/api/posting-detail/'+str(id))

def mypage_view(request,username):
    if request.method == 'GET':
        # mypage = UserInfo.objects.get(id=id)

        # return redirect('/api/mypage'+str(username))

        return render(request, 'posting/mypage.html')
        # return render(request, 'tweet/tweet_detail.html', {'tweet': my_tweet, 'comment': tweet_comment})


