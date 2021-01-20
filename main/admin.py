from django.contrib import admin
from .models import AdvUser
from .models import SuperRubric, SubRubric
from .forms import SubRubricForm
from .models import Bb, AdditionalImage
from .models import Comment



import datetime


class SubRubricInline(admin.TabularInline):
    model = SubRubric


class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)


class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage


class BbAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'author', 'created_at')
    fields = (('rubric', 'author'), 'title', 'content',
             'image', 'is_active')
    inlines = (AdditionalImageInline,)


admin.site.register(AdvUser)
admin.site.register(SuperRubric, SuperRubricAdmin)
admin.site.register(SubRubric, SubRubricAdmin)
admin.site.register(Bb,BbAdmin)
admin.site.register(Comment)



