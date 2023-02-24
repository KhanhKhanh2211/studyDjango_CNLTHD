from rest_framework. serializers import ModelSerializer
from .models import Couser, Tag, Lesson, User, Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Couser
        fields = '__all__'

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]

class LessonSerializer(ModelSerializer):
    tags = TagSerializer(many = True)
    class Meta:
        model = Lesson
        fields = ["id", "subject", "content","create_date","image" , "Couser", "tags"]
    

class UserSeriazlier(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name','email','username','password','avatar']
        #khong show display "password"
        # extra_kwargs = {
        #         'password':{'write_only':'true'}
        #     }

    #create User
    def create(self, validated_data):
        # '**' thuc hien lay all truong
        #user = User(**validated_data)
        user = User()
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.email = validated_data['email']
        user.username = validated_data['username']
        user.set_password( validated_data['password'])
        user.avatar = validated_data['avatar']
        user.save()
        return user


    # def update(self, pk, validated_data):
    #     user = User.objects.get(pk=pk)
    #     user.first_name = validated_data['first_name']
    #     user.last_name = validated_data['last_name']
    #     user.email = validated_data['email']
    #     user.username = validated_data['username']
    #     user.set_password( validated_data['password'])
    #     user.avatar = validated_data['avatar']
    #     user.save()
    #     return user

   
        

       