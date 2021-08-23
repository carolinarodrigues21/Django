from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice 
    extra = 3
class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [

        #title f the field set, field info
        (None,                {'fields': ['question_text']}),
        ('Date informaition', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

