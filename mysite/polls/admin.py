from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [

        #title f the field set, field info
        (None,                {'fields': ['question_text']}),
        ('Date informaition', {'fields':['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
