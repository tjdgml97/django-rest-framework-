from django.http import Http404, HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . import models 
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone

from .models import Choice, Question

#수정
def index(req:HttpRequest) -> HttpResponse:
    # if not req.user.is_anonymous :
    #     print(req.user.email)

    latest_question_list  = models.Question.objects.filter(pub_date__lt =timezone.now()).order_by('-pub_date')[:5]
    # if req.session.get('count') is None:
    #     req.session['count'] = 0
    # req.session['count'] += 1
    # print(req.session['count'])

    res = render(req, 'polls/index.html', {'latest_question_list': latest_question_list})
    # res.set_cookie('univ', 'hgu')
    return res


# def index(req:HttpRequest):
#     latest_question_list = models.Question.objects.order_by('-pub_date')[:5]
#     req.session['univ']='hgu session'
#     res = render(req, 'polls/index.html', {'latest_question_list':latest_question_list})
#     res.set_cookie('univ','hgu')
#     return res
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    


def detail(req, question_id):
    # print(req.COOKIES['univ'])
    # print(req.session['count'])
    question = models.Question.objects.filter(pk=question_id)
    if len(question) == 0 or question.pub_date > timezone.now():
        raise Http404("Question does not exist")
    return render(req, 'polls/detail.html', {'question': question[0]})


# class DetailView(generic.DetailView):
#     ...
#     def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Question.objects.filter(pub_date__lte=timezone.now())
