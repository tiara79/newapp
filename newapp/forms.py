# 21/04/14 전은주 장고 폼 페이지 작성
from .models import Question, Answer, Comment
from django import forms

# django > forms > ModelForm을 가져옴
# 내부 클래스 Meta의 model, fields는 일반변수
class QuestionForm(forms.ModelForm):
  class Meta:
     # Meta(css) 클래스 안에 model,fields,widgets(컬럼)들의 속성이 있다.
     # TextInput는 한줄, Textarea는 여러줄
     model = Question
     fields = ['subject', 'content']
     labels = {
         # 영어 -> 한글로 커스터마이징 한다.그러나 이것을 사용하면 디자이너가 어렵다.
         'subject': '글 제목',
         'content': '내용',
     }
     widgets = {'subject': forms.TextInput(attrs={'class': 'form-control'}),
                'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
              }


class AnswerForm(forms.ModelForm):
  class Meta:
      model = Answer
      fields = ['content2']
      labels = {'content2': '답변내용', }

# 21/04/22 전은주 장고 댓글 폼 페이지 작성
class CommentForm(forms.ModelForm):
  class Meta:
      model = Comment
      fields = ['content']
      labels = {'content': '댓글내용', }


















