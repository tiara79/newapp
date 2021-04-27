from django.db import models
# ----[edit 21/04/20 user 테이블에 정보를 가져옴 ]
from django.contrib.auth.models import User

# 질문의 속성(칼럼)
# 질문 제목: subject
# 내용: content
# 일자: create_date
# 저자(글쓴이): author

# 답변내용 : content
# 일자 : create_date2
# 일자: create_date
# 저자(글쓴이): author

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    # author 컬럼은 User 테이블의 외래키로 적용시킴
    # on_delete=models.CASCADE 계정이 삭제되면 계정과 연결된 Question
    # 테이블 데이터를 모두 삭제
    # 중복 id 제외, 바코드 id 제외
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # null 을 허용하고 싶을때 사용방법
    # [21/04/26] author 에 related_name='author_question' 수정
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    modify_date = models.DateTimeField(null=True, blank=True)
    # [21/04/26] 추천 컬럼 추가 (컬럼간의 N:M관계 문법(속성:ManyToManyField))
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content2 = models.TextField()
    create_date2 = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    # [edit 21/04/21]  ----------------------#
    # blank = form.is_valid 에서 데이터 검사시 값이 없어도 된다는 의미.
    modify_date = models.DateTimeField(null=True, blank=True)
    # [21/04/26] 추천 컬럼 추가 (컬럼간의 N:M관계 문법(속성:ManyToManyField))
    voter = models.ManyToManyField(User, related_name='voter_answer')

    def __str__(self):
        return self.content2

# [edit 21/04/22]  글쓴이,질문,답글 외래키 만들기 ----------------------#
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)





















