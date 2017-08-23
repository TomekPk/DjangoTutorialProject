
from django.http import HttpResponseRedirect, HttpResponse
from .models import MyQuestion, MyChoice
# from django.shortcuts import render # it is common idiom to load a template
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

'''
# LONG VIEW using HttpResponse
def main_view(request):
    latest_question_list = MyQuestion.objects.order_by('-pub_date')[:5]
    template = loader.get_template('app1/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context,request))
'''

# SHORT VIEW using render shortcut function from django.shortcut
def main_view(request):
    latest_question_list = MyQuestion.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,'app1/index.html', context)

def contact_view(request):
    return HttpResponse("You are at the contact_view")

def appinfo_view(request):
    return HttpResponse("You are at the appinfo_view")

# View with 404
def detail_view(request, question_id):
    # 1.method 404:
    '''
    try:
        question = MyQuestion.objects.get(pk=question_id)

    except MyQuestion.DoesNotExist:
        return render(request, 'app1/404.html') #with render and 404.html
        #or: raise Http404("Question does not exist") #without render
    '''
    # 2.method 404:
    question = get_object_or_404(MyQuestion, pk=question_id)
    return render(request,'app1/detail.html',{'question':question})

def results_view(request, question_id):
    question = get_object_or_404(MyQuestion, pk=question_id)
    return render(request, 'app1/results.html', {'question': question})
    #return HttpResponse("You are at the results_view and You are looking at question %s." % question_id)

def vote_view(request, question_id):
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
        return HttpResponseRedirect(reverse('app1:results_view', args=(question.id,)))
    #return HttpResponse("You are at the vote_view and You are looking at question %s" % question_id)
