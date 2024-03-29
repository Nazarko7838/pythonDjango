from django.urls import path, include
from .views import render_main_page, create_question, render_categories_page, create_answer, \
    render_question_page, user_questions, edit_answer, edit_question, search, ask_question, \
    vote, delete_notification, delete_object

urlpatterns = [
    path('', render_main_page, name='render_main_page'),
    path('create_question', create_question,  name='create_question'),
    path('categories', render_categories_page, name='render_categories_page'),
    path('create_answer', create_answer, name='create_answer'),
    path('question', render_question_page, name='render_question_page'),
    path('question/edit/<int:question_id>/', edit_question, name='edit_question'),
    path('answer/edit/<int:answer_id>/', edit_answer, name='edit_answer'),
    path('my_questions', user_questions, name='user_questions'),
    path('search', search, name='search'),
    path('ask_question', ask_question, name='ask_question'),
    path('<str:object_name>/delete/<int:object_id>/', delete_object, name='delete_object'),

    path('cancel_delete', user_questions, name='cancel_delete'),
    path('<model>/<action>/<int:record_id>/', vote, name='vote'),
    path('delete_notification/<int:notification_id>', delete_notification, name='delete_notification')
]
