from django.contrib import admin

from .models import MyQuestion, MyChoice

admin.site.register(MyChoice)

'''
admin.site.register(MyChoice)

class ChoiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Your Choice:",                  {'fields': ['choice_text']}),
        ('Votes information:',   {'fields': ['votes']}),
    ]

admin.site.register(MyChoice, ChoiceAdmin)
'''

class ChoiceInline(admin.TabularInline):
    model = MyChoice
    extra = 6

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information:',   {'fields': ['pub_date'], 'classes': ['collapse']}), # collapse-> show/hide option
    ]
    inlines = [ChoiceInline]
    list_display =  ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    # fields=['pub_date','question_text'] #Konkretnie ta zmiana powyżej powoduje, że „Publication date” jest przed polem „Question”:

admin.site.register(MyQuestion, QuestionAdmin)
