from django.contrib import admin
from .models import Question, QuestionGroup, SolvedQuestionGroup
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option')
    search_fields = ('question_text',)
@admin.register(QuestionGroup)
class QuestionGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "creater", "time")
    search_fields = ('name',"creater")
    filter_horizontal = ('questions',)

@admin.register(SolvedQuestionGroup)
class SolvedQuestionGroupAdmin(admin.ModelAdmin):
    list_display = ('user', 'question_group', 'score')
    search_fields = ('user__user__username', 'question_group__name')