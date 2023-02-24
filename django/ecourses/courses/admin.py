from django.contrib import admin
from .models import Category, Couser, Lesson, Tag, User, Comment
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.html import  mark_safe
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        models = Lesson
        fields = '__all__'

# nhung Tag vao from Lesson
class LessonTangInline(admin.TabularInline):
    model = Lesson.tags.through

#custom form Lesson
class LessonAdmin(admin.ModelAdmin):
    class Media:
        css = {
            #'all':('/static/css/main.css',)
        }                                 # DANG #BUG
    form = LessonForm

    #show display user properties('thuoc tinh')
    list_display = ["id","subject", "create_date","active","Couser"]
    list_filter = ['subject','create_date']
    search_fields = ['subject', 'create_date'] 
    readonly_fields = ['avatar'] 
    inlines = (LessonTangInline, )

    #function that returns a mark_safe link
    #hàm có chức năng trả về một mark_safe link 
    def avatar(sefl, lesson):
        return mark_safe("<img scr ='/static/{img_url}' alt= '{alt}' width = '120x'/>".format(img_url = lesson.image.name, alt = lesson.subject))

#nhúng tag vào lesson (site:add lesson)
class LessonInline(admin.StackedInline):
    model = Lesson
    pk_name = 'Couser'

class CourseAdmin(admin.ModelAdmin):
    inlines = (LessonInline,)


#Custom Site Admin

class CourseAppAdminSite(admin.AdminSite):
    #def custom_header(sefl, request):
       # return TemplateResponse(request,'admin/admin-site.html')
    site_header = ('Hệ thống quản lý khóa học')
    site_title = 'admin'
    site_url = 'Hệ thống quản lý khóa học'
    def get_urls(self):
        return [
            path('course-stats/', self.course_stats)
        ] + super().get_urls()
    #custom site admin coutn Cousers
    def course_stats(self, request):
        course_count = Couser.objects.count()
        stats = Couser.objects.annotate(lesson_count = Count('lessons')).values('id', 'subject','lesson_count')#ten mac dinh lessons
        return TemplateResponse(request, 'admin/courses-site.html', {
            'course_coutn': course_count,
            'stats' : stats
        })


admin_site = CourseAppAdminSite('mycourse')


# Register your models here
admin_site.register(Couser, CourseAdmin)
admin_site.register(Category)
admin_site.register(Lesson,LessonAdmin)
admin_site.register(User)
admin_site.register(Tag)
admin_site.register(Comment)


#admin.site.register(Couser, CourseAdmin)
#admin.site.register(Category)
#admin.site.register(Lesson,LessonAdmin)