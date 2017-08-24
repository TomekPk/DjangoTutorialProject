
from django.http import HttpResponseRedirect, HttpResponse
from .models import MyQuestion, MyChoice
# from django.shortcuts import render # it is common idiom to load a template
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'app1/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return MyQuestion.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = MyQuestion
    template_name = 'app1/detail.html'


class ResultsView(generic.DetailView):
    model = MyQuestion
    template_name = 'app1/results.html'

def vote(request, question_id):
    question = get_object_or_404(MyQuestion, pk=question_id)
    try:
        selected_choice = question.mychoice_set.get(pk=request.POST['choice'])
    except (KeyError, MyChoice.DoesNotExist):
        return render(request, 'app1/detail.html', {
        'question':question,
        'error_message': "You didn't select choice.",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('app1:results', args=(question.id,)))
    #return HttpResponse("You are at the vote_view and You are looking at question %s" % question_id)
