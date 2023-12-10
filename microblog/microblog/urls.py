from django.contrib import admin
from django.urls import path

from blog.views import frontpage

# admin/にアクセスるとadmin.siteurlsに飛ぶ。
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", frontpage)
]
