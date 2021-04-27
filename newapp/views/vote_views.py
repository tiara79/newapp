#  21/04/26  vote_views 파일 생성
from django.shortcuts import render, get_object_or_404, redirect

#  21/04/27  vote_views 작성
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from newapp.models import Question, Answer

@login_required(login_url='common:login')
def vote_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # 로그인한 유저와 질문을 쓴 유저가 같은지를 확인
    if request.user == question.author:
        messages.error(request, '본인 질문 글은 추천 할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('newapp:detail', question_id=question.id)

# [21/04/27] vote_answer 함수 생성
@login_required(login_url='common:login')
def vote_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user == answer.author:
        messages.error(request, '본인 답변글은 추천 할 수 없습니다.')
    else:
        answer.voter.add(request.user)
    return redirect('newapp:detail', question_id=answer.question.id)
