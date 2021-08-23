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

    list_display = ('question_text','pub_date', 'was_published_recently')

    #adds a filter to the page
    list_filter = ['pub_date']

    #adds a search box at the top of the list
    search_fields=['question_text']

admin.site.register(Question, QuestionAdmin)

