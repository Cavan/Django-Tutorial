from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.urls import reverse


from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, Question


class IndexView(generic.ListView):
    """[summary]

    :param generic: [description]
    :type generic: [type]
    :return: [description]
    :rtype: [type]
    """
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """[summary]

        :return: [description]
        :rtype: [type]
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """[summary]

    :param generic: [description]
    :type generic: [type]
    :return: [description]
    :rtype: [type]
    """
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """[summary]

        :return: [description]
        :rtype: [type]
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    

class ResultsView(generic.DetailView):
    """[summary]

    :param generic: [description]
    :type generic: [type]
    """
    model = Question
    template_name = 'polls/results.html'



def vote(request, question_id):
    """[summary]

    :param request: [description]
    :type request: [type]
    :param question_id: [description]
    :type question_id: [type]
    :return: [description]
    :rtype: [type]
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question' :question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing 
        # with POST data. This prevent data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))