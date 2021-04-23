# 21/04/15 전은주 템플릿 필터 모듈 및 함수 작성
from django import template

register = template.Library()

@register.filter()
def sub(value, arg):
    return value-arg