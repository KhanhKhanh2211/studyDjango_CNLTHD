from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Couser,Lesson,Tag, User, Comment
from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import action
from .serializers import CourseSerializer, LessonSerializer, UserSeriazlier, CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
class CommentAPIView(APIView):
    def get(self, request, lesson_id):
        comments = Comment.objects.filter(lesson_id = lesson_id)
        serializer = CommentSerializer(comments, many = True)
        
        return Response(serializer.data, status= status.HTTP_200_OK)
    

    def post(self, request,lesson_id):
        content = request.data.get('content')
        if content is not None:
            try: 
                c = Comment.objects.create(content = content , user = request.user, lesson_id = lesson_id)
            
            except IntegrityError:
                err_msg = "Lesson does not exits!"
            else:
                return Response(CommentSerializer(c).data, status= status.HTTP_201_CREATED)
        else:
            err_msg = "Content is Required!!"

        return Response(data={'error_msg':err_msg}, status=status.HTTP_400_BAD_REQUEST)




# rest_framework
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Couser.objects.filter(active=True)
    serializer_class = CourseSerializer
    #Phương thức chứng thực user
    permission_classes = [permissions.IsAuthenticated]

    #Ghi dè phương thức chứng thực user
    # user ko đăng nhập vẫn xem được nội dung
    # def get_permissions(self):
    #     if self.action == 'list':
    #         return[permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]
    
    # Tự động tạo sẵng 
    #List(Get) -> show khóa khọc
    #.. (POST) -> Them khoa hoc
    #detail -> Xem chi tiết 1 khóa học
    #...(PUT) -> Cập nhật
    #...(DELETE) -> Xóa khóa học







class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active = True)
    serializer_class = LessonSerializer
    @action(methods=['post'], detail=True, url_name= "hide-lesson")
    #/lesssons/{pk}/hide-lesson
    def hide_lesson(self, request, pk):
        try:
            l = Lesson.objects.get(pk=pk)
            if l.active == True:
                l.active = False
                l.save()
            else:
                l.active = True
                l.save()
        except Lesson.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(data=LessonSerializer(l, context={'request': request}).data, status=status.HTTP_200_OK)
    
    #add tag cho lesson
    @action(methods=['post'], detail= True, name="add tags to a lesson",url_path='add-tags-to-lesson', 
url_name='add-tags')
    def add_tags_to_lesson(self, request, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
            tags = request.data.get('tags')
            for tag in tags.split(','): 
                t, _ = Tag.objects.get_or_create(name=tag.strip())
                lesson.tags.add(t)
            lesson.save()
        except Lesson.DoesNotExist | KeyError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LessonSerializer(lesson)
        return Response(serializer.data, status=status.HTTP_200_OK)





class UserViewSet(viewsets.ViewSet, generics.CreateAPIView,
        generics.RetrieveAPIView, generics.ListAPIView, generics.UpdateAPIView):
    queryset = User.objects.filter(is_active = True)
    serializer_class = UserSeriazlier
    parser_classes = [MultiPartParser,]
    
    # def get_permissions(self):
    #     if self.action == 'retrieve':
    #         return [permissions.IsAuthenticated()]
    #     return [permissions.AllowAny()]

    # @action(methods=['post'], detail=True, url_name="update-user")
    # def Updata(self, request, pk):
    #     try:
    #         l = User.objects.get(pk=pk)
    #         l.first_name = 'first_name'
    #         l.last_name = 'last_name'
    #         l.email = 'email'
    #         l.set_password('password')
    #         l.avatar = 'avatar'
    #         l.save()
    #     except Lesson.DoesNotExist:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    #     return Response(data=LessonSerializer(l, context={'request': request}).data, status=status.HTTP_200_OK)

#class UserViewSet_Update()

#-----------------------------------------------------------------------------------------------------------


#Khanh Custom 200 ok 
def index(request):
    return render(request ,template_name='index.html', context={
        'name':'Khanh Duong'
    })


def test(request):
    couser = Couser.objects.all().values()
    template = loader.get_template('test.html')
    context = {
        'Couser': couser,
    }
    return HttpResponse(template.render(context,request))

#khanh custom Hiện thị sản phẩm + html '200 OK'
def product(request):
    proDuct = Couser.objects.all().values()
    #cateGory = cateGory[:10]
    template = loader.get_template('product.html')
    context = {
        'proDuct': proDuct,
    }
    return HttpResponse(template.render(context,request))


def detail(request,id):
    couser = Couser.objects.get(id = id)
    template = loader.get_template('detail.html')
    context = {
        'Couser': couser,
    }
    return HttpResponse(template.render(context,request))



def wellcom(request,year):
    return HttpResponse("hello" + str(year))

def wellcom2(request,year):
    return HttpResponse("hello" + str(year))


