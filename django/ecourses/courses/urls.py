from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from . admin import admin_site
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('courses',views.CourseViewSet)
router.register('lessons',views.LessonViewSet)
router.register('user',views.UserViewSet)
#router.register()
#tạo ra 2 empoint 
#/courses/- Get
#/courses/ - POST
#/courses/{course_id} - GET
#/courses/{course_id} - PUT
#/courses/{course_id} - DELETE

urlpatterns = [
    path('', include(router.urls)),

    #Khanh custom
    #path('TEST/', views.index, name="index"),
    #path('test/', views.test, name='dmTest'),
    #path('product/', views.product, name='SanPham'),
    path('admin/', admin_site.urls),
    #path('welcome/<int:year>/', views.wellcom, name="welcome"),
    path('lessons/<int:lesson_id>/comments/',views.CommentAPIView.as_view())
    #Bieu thuc chinh quy
    #re_path(r'^welcome2/(?P<year>[0-9]{1,3})/$', views.wellcom2, name='as'),

    #url -> detail 1 giá trị (database Courses)
    #path('test/detail/<int:id>', views.detail, name="detail<int:id>")
]
    