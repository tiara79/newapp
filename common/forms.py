# ----------------- [21/04/19]  회원가입 폼 작성 -----------------
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# UserCreationForm 을 이용해서 회원가입의 기본 속성을 받아 올 수 있다.
# 받아오는 기본 속성은 username,password1,password2를 받아 올 수 있다.
# Email 등 다른 속성들을 추가 해서 회원 가입시 입력하게 만들 수 있다.
# username : 사용자명(id)
# password1 : 비밀번호
# password2 : 비밀번호확인

class UserForm(UserCreationForm):
   email = forms.EmailField(label='email')

   class Meta:
      model = User
      fields = ("username", "email")

# Meta 클래스: UserForm 의 내부 클래스
