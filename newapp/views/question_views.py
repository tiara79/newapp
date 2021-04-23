# [21/04/23] views.py 모듈 분리

# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
# ---------------------- [edit] ----------------- #
# from django.http import HttpResponse
from django.utils import timezone
#  [edit 21/04/15 ] 페이징 처리 추가 ----------------- #
from django.core.paginator import Paginator
# [21/04/20] 질문,답변 수정 ----------------------#
from django.contrib.auth.decorators import login_required
# [21/04/21] 질문 수정 ----------------------#
from django.contrib import messages

# 21/04/14 전은주 urls.py의 question_create 만들기(장고폼 : 질문 등록 함수 생성)
# [edit 21/04/20]  ----------------------#
from newapp.forms import QuestionForm
from newapp.models import Question

@login_required(login_url='common:login')
# ----------------------------------------#
def question_create(request):
  if request.method == 'POST':
     form = QuestionForm(request.POST)
     if form.is_valid():
         # 폼에 입력한 값들을 임시 저장(commit 기본 설정 True)
         question = form.save(commit=False)

         # [21/04/20] author 추가 적용
         question.author = request.user

         question.create_date = timezone.now()
         # create_date 컬럼을 받아서
         # 저장(이유: create_date 컬럼을 폼에서 받아오지 않아서
         # 컬럼에 저장될 내용을 추가한후 저장함
         question.save()
         # ':index' index 함수로 반환
         return redirect('index')
  else:
     form = QuestionForm()

  # return: main으로 이동
  return render(request, 'newapp/question_form.html', {'form': form})

# [edit 21/04/21] 질문 수정 부분----------------------#
@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('newapp:detail', question_id=question_id)

    # instance : 폼에서 받아온 내용의 내부 구조를 정의 할때 사용
    # 사용 이유: 기존의 데이터를 받아와서 내용을 수정 하기 위해 선언
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        # .is_valid(): 오류성검사  .author: 글쓴이
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('newapp:detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)
        return render(request, 'newapp/question_form.html', {'form': form})

# [edit 21/04/21] 질문 삭제 부분----------------------#
@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('newapp:detail', question_id=question_id)

    question.delete()
    return redirect('newapp:index')
