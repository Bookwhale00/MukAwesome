from django.shortcuts import render, redirect
from .models import UserInfo
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UpdateUserInfo
from django.contrib import messages


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
                UserInfo.objects.create_user(username=username, password=password, email=email)
                return redirect('/api/sign-in')
            
            
def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")

        me = auth.authenticate(request, username=username, password=password)
        if me is not None:
            auth.login(request, me)
            return redirect('/api/profile/')
            # 임시로 로그인 성공하면 profile페이지로 가도록 해놨습니다!
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
    return redirect('/api/sign-in/')


# 프로필보기
@login_required # 로그인해야 볼 수 있다.
def profile_view(request):
    """
    GET = 현재 로그인 한 사람 데이터 가져오기
    """
    if request.method == 'GET':
        return render(request, 'user/profile.html')
    
# 프로필 수정
@login_required
def profile_update_view(request):
    """
    GET = 페이지 들어갔을 때 html 렌더하기
    POST = 입력하고 수정완료 클릭했을 때 데이터가 유효하면(is_valid) UpdateUserInfo클래스를 통해 DB의 값이 수정되서 들어가고, 아니면 수정페이지가 다시 렌더됨->수정필요!
    """
    if request.method == 'POST':
        update_profile = UpdateUserInfo(request.POST, instance = request.user)

        if update_profile.is_valid():
            update_profile.save()
            messages.success(request, '프로필이 수정되었습니다.')
            # 데이터는 들어가는데 메세지가 왜 안뜰까? 
            return render(request, 'user/profile.html')
        else:   # 유효성 검사 실패했을 때인데, 맞는 에러메시지가 출력되도록 수정 필요함
                # 지금은 수정페이지가 다시 렌더됨.
                # 큐... Q 머시기 찾아보기
                # 정규표현식! mbti는 16개 중에 선택하도록 (드롭다운메뉴)
            update_profile = UpdateUserInfo(instance = request.user)

            return render(request, 'user/profile-update.html', {'update_profile':update_profile})
        
    elif request.method == 'GET':
        return render(request, 'user/profile-update.html')