# ---------------------- [edit] ----------------- #
from django.urls import path

# ---------------------- [edit] ----------------- #
# url 에 별칭 부여하기(name='')
# 실제 주소명 /newapp/은 index 라는 URL 별칭으로 변경
# 실제 주소명 /newapp/question_id/는 detail 라는 URL 별칭으로 변경
# --------[네임 스페이스 : 각각의 앱이 관리 하는 공간] --------- #
# 네임스페이스 변수를 만든다면 저장되는 문자열값은 앱 이름과 동일하게 하는것이 편하다.
app_name = 'newapp'
# ------------------------------------------------------- #
# 앱(newapp)을 추가할때 다른 앱(config/urls.py)하고 url 별칭이 중복되면 안된댜
# 2021.04.13 전은주 게시글 클릭시 들어갈 페이지 추가
# 게시글 답변작성 페이지 추가 (한 후 views.py에 함수 만든다)

# ---------------------- [21/04/23 edit] ----------------- #
# -----------------------[21/04/27 edit vote_views import 추가]------------------------ #
from .views import answer_views, base_views, comment_views, question_views, vote_views

urlpatterns = [
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),

# 2021.04.14 전은주
    path('question/create/', question_views.question_create, name='question_create'),
# 2021.04.21 질문의 수정부분
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name='question_delete'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

# 2021.04.22 질문과 답변 분리(댓글이 없거나 아이디가 없을경우)
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'),

    path('comment/create/answer<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),

# 2021.04.26 질문 추천 기능 주소 추가
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
# 2021.04.27 답변 추천 기능 주소 추가
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),
]

