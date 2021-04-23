from django.contrib import admin
# ---------------------- [edit] ----------------- #
from .models import Question
# ----------------------------------------------- #

# ---------------------- [edit] ----------------- #
# 검색 필드 생성
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
# ----------------------------------------------- #
# Register your models here.