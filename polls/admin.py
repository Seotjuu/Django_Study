from django.contrib import admin

from .models import Question

admin.site.register(Question)   # 관리자 사이트에서 poll app 가능하게 하기

# admin 페이지에서 데이터 추가 및 수정 가능함