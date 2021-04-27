#  21/04/26  vote_views 파일 생성
from django.shortcuts import render, get_object_or_404

#  21/04/27  vote_views 작성
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from newapp.models import Question, Answer


