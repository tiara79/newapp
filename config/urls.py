"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# ---------------------- [edit2] ----------------- #
from django.urls import path, include
# ---------------------- [edit-0416] ----------------- #
# from newapp import views
from newapp.views import base_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('newapp/',views.index),
    # newapp/으로 시작되는 요청은 모두 newapp/urls.py 파일에 있는
    # 매핑을 참고해서 처리 하라는 의미 (url 분리)
    path('newapp/', include('newapp.urls')),
    # 이러한 선언으로 요청은 앞으로 newapp/urls.py 에서
    # 관리 한다는 것으로 인식한다.
    # 21/04/16 common.urls 연결
    path('common/', include('common.urls')),
    # 21/04/23 view 모듈 분리 후 연결(기존 루트 변경)
    path('', base_views.index, name='index'),
]
