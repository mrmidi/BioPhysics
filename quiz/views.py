from django.shortcuts import render
from .models import Question, Topic
from django.shortcuts import get_object_or_404
import random

from django.http import JsonResponse


def check_answer(request, question_id):
    if request.method == "POST":
        selected_answers = [int(answer) for answer in request.POST.getlist('answers[]')]
        question = get_object_or_404(Question, pk=question_id)

        correct_answers = [answer.id for answer in question.answers.filter(is_correct=True)]
        displayed_answers = request.session.get('displayed_answers', [])
        print("Displayed answers: ", displayed_answers)

        not_selected_answers = [answer for answer in displayed_answers if answer not in selected_answers]

        # Now, let's calculate the score:
        score = 1

        # remove 0.25 for each wrong answer
        for answer in selected_answers:
            if answer not in correct_answers:
                score -= 0.25

        # penalize for not selecting correct answers
        for answer in correct_answers:
            if answer not in selected_answers and answer in displayed_answers:  # Ensure answer is among the displayed answers
                score -= 0.25

        score = max(0, score)  # Ensure score is not negative

        return JsonResponse({
            'correct_answers': correct_answers,
            'selected_answers': selected_answers,
            'not_selected_answers': not_selected_answers,
            'score': score
        })




def study_mode(request, question_id=None):
    if question_id:
        question = get_object_or_404(Question, pk=question_id)
    else:
        # If no specific question ID is provided, you can choose to:
        # a) Redirect to a random question
        # b) Pick the first question or any other logic you prefer
        question = Question.objects.first()

    all_answers = list(question.answers.all())
    displayed_answers = random.sample(all_answers, min(4, len(all_answers)))
    request.session['displayed_answers'] = [answer.id for answer in displayed_answers]
    topics = Topic.objects.all()

    context = {
        'question': question,
        'displayed_answers': displayed_answers,
        'topics': topics,
    }

    return render(request, 'quiz/study_mode.html', context)
