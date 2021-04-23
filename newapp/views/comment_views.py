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

# [edit 21/04/22] 질문 댓글달기 기능 부분----------------------#
from newapp.forms import CommentForm
from newapp.models import Question, Comment, Answer


@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('newapp:detail', question_id=question_id)
    else:
        form = CommentForm()
    return render(request, 'newapp/comment_form.html', {'form': form})

# [edit 21/04/22] 질문 댓글 수정 기능 부분----------------------#
@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('newapp:detail', question_id=comment.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('newapp:detail', question_id=comment.question.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'newapp/comment_form.html', {'form': form})

# [edit 21/04/22] 댓글 삭제 기능 부분----------------------#
@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('newapp:detail', question_id=comment.question.id)
    else:
        comment.delete()
    return redirect('newapp:detail', question_id=comment.question.id)

# [edit 21/04/22]  위(comment_create_answer ~ comment_delete_answer)에서 복사해옴
@login_required(login_url='common:login')
def comment_create_answer(request, answer_id):

    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('newapp:detail', question_id=comment.answer.question.id)
    else:
        form = CommentForm()
    return render(request, 'newapp/comment_form.html', {'form': form})

# [edit 21/04/22] 질문 댓글 수정 기능 부분----------------------#
@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('newapp:detail', question_id=comment.answer.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('newapp:detail', question_id=comment.answer.question.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'newapp/comment_form.html', {'form': form})

# [edit 21/04/22] 댓글 삭제 기능 부분----------------------#
@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('newapp:detail', question_id=comment.answer.question.id)
    else:
        comment.delete()
    return redirect('newapp:detail', question_id=comment.answer.question.id)
