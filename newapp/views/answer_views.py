
# [21/04/23] views.py 모듈 분리
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

# [edit 21/04/21] 답변 수정 부분----------------------#
from newapp.forms import AnswerForm
from newapp.models import Answer, Question


# [edit 21/04/20]  ----------------------#
@login_required(login_url='common:login')
# ---------------------------------------#
# 21/04/13 전은주 urls.py의 answer_create 만들기
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # content은 question_detail.html의 textarea, timezone은 from django.utils import timezone

    # [21/04/20]  추가 적용
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            # 폼에 입력한 값들을 임시 저장(commit 기본 설정 True)
            answer = form.save(commit=False)
            #     question.answer_set.create(content2=request.POST.get('content2'), create_date2=timezone.now())
            #     # detail(주소 별칭), redirect import 해줘야 함
            #     # question_id(answer_create의 파라미터) = question_id( question 테이블에 id)
            #     return redirect('newapp:detail', question_id=question_id)

            # [21/04/20] author 추가 적용
            answer.author = request.user
            answer.create_date2 = timezone.now()
            answer.question = question
            # create_date 컬럼을 받아서
            # 저장(이유: create_date 컬럼을 폼에서 받아오지 않아서
            # 컬럼에 저장될 내용을 추가한후 저장함
            answer.save()
            # ':index' index 함수로 반환
            return redirect('newapp:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question1': question, 'form': form}
    # return: main으로 이동
    return render(request, 'newapp/question_detail.html', context)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('newapp:detail', question_id=answer.question.id)

    # instance : 폼에서 받아온 내용의 내부 구조를 정의 할때 사용
    # 사용 이유: 기존의 데이터를 받아와서 내용을 수정 하기 위해 선언
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        # .is_valid(): 오류성검사  .author: 글쓴이
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('newapp:detail', question_id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
        return render(request, 'newapp/answer_form.html', {'answer': answer, 'form': form})

# [edit 21/04/21] 답변 삭제 부분----------------------#
@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('newapp:detail', question_id=answer.question.id)
    else:
        answer.delete()
    return redirect('newapp:detail', question_id=answer.question.id)