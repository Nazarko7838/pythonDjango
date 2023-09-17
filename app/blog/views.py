from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .controllers import *
from .forms import *
from .models import Notification
# TODO add function thet crates answer

def render_main_page(request):

    category_id = request.GET.get('id')
    if category_id:
        questions = get_all_questions_with_answers_for_category(category_id)
    else:
        questions = get_all_questions_with_answers()
    print(questions)
    for i in questions:
        print(f'{i} - object')
        print(f'{i.answer_set.all()} - answers')

    return render(request, 'main.html', context={'questions': questions})



def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            create_question_with_success_message(form,request)
        else:
            messages.error(request, 'There was an error while adding question, check your data and try again.')
        return redirect('/')


def render_categories_page(request):
    categories = get_all_categories()
    return render(request, 'categories.html', {'categories': get_all_categories()})


def create_answer(request):

    if request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            create_answer_with_success_message(form, request)
        else:
            messages.error(request, 'There was an error while adding question, check your data and try again.')
        return redirect('/')


def render_question_page(request):
    question_id = request.GET.get('id')
    answer_form = AnswerForm()
    return render(request, 'question.html', {'question': get_question_by_id(question_id),
                                             'answers': get_answers_for_question(question_id).order_by('-up_votes'),
                                             'answer_form': answer_form})



def render_categories_categories_page(request):
    categories = get_all_categories()
    return render(request, 'categories.html', {'categories': categories})


def edit_question(request, question_id):
    return edit_record(request, Question, QuestionForm, question_id)


def edit_answer(request, answer_id):
    return edit_record(request, Answer, AnswerForm, answer_id)


def delete_question(request, question_id):
    return delete_record(request, Question, question_id)


def delete_answer(request, answer_id):
    return delete_record(request, Answer, answer_id)


def user_questions(request):
    questions = get_all_questions_for_user(request.user)
    answers = get_all_answers_for_user(request.user)
    notifications = get_all_notifications_for_user(request.user)
    return render(request, 'user.html', {'questions': questions, 'answers': answers, 'notifications': notifications})


def search(request):
    search_query = request.GET.get('query')
    questions = get_questions_by_search_query(search_query)
    return render(request, 'main.html', {'questions': questions})

def ask_question(request):
    question_form = QuestionForm()
    return render(request, 'ask_question.html', context={'question_form': question_form})


def delete_object(request, object_id, object_name):
    match object_name:
        case 'question':
            return delete_record(request, Question, object_id)
        case 'answer':
            return delete_record(request, Answer, object_id)


def delete_notification(request, notification_id):
    Notification.objects.filter(pk=notification_id).delete()
    print(Notification.objects.all())
    return HttpResponse('')


def vote(request, model, action, record_id):
    model_mapping = {
        'question': Question,
        'answer': Answer
    }
    model_class = model_mapping.get(model)

    record = get_object_or_404(model_class, pk=record_id)

    if isinstance(record, Answer):
        redirect_id = record.question.id
    else:
        redirect_id = record_id

    try:
        if action == 'upvote':
            record.upvote(request.user.id)
        elif action == 'downvote':
            record.downvote(request.user.id)

        if request.user != record.author:
            create_notification(request, record, action)
        resp_data = 'ok'
    except Exception as e:
        print(e)
        resp_data = str(e)

    response = HttpResponse(resp_data)
    return redirect(f'/question?id={redirect_id}')