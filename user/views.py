from django.shortcuts import render, redirect
from .models import UserInfo
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email', '')

        if password != password2:
            return render(request, 'user/signup.html', {'error': '패스워드를 확인 해 주세요!'})
        else:
            if username == '' or password == '':
                return render(request, 'user/signup.html', {'error': '사용자 이름과 패스워드는 필수 값 입니다'})

            exist_user_name = get_user_model().objects.filter(username=username)
            exist_user_email = get_user_model().objects.filter(email=email)
            # exist_user_password = get_user_model().objects.filter(password=password)
            if exist_user_name:
                return render(request, 'user/signup.html', {'error':'사용자가 존재합니다.'})
            elif exist_user_email:
                return render(request, 'user/signup.html', {'error':'사용자가 존재합니다.'})
            # elif exist_user_password:
            #     return render(request, "user/signup.html", {'error':'사용중인 비밀번호 입니다.'})
            else:
                print(exist_user_name)
                UserInfo.objects.create_user(username=username, password=password, email=email)
                return redirect('/sign-in')
            
            
def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/')
        else:
            return render(request,'user/signin.html',{'error':'유저이름 혹은 패스워드를 확인 해 주세요'})
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signin.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

# 프로필보기
@login_required # 로그인해야만 볼 수 있다.
def profile_view(request):
    """
    GET : 현재 로그인한 사람의 프로필을 보여줍니다.
    PUT : 현재 로그인한 사람의 프로필을 수정합니다. 
    """
    profiles = UserInfo.objects.all()
    data = []

    for profile in profiles:
        data.append({
            "사용자 아이디":UserInfo.username,
        })
    return HttpResponse(data)