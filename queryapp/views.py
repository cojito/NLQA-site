from django.shortcuts import render_to_response
from django.shortcuts import render 
from django.http import HttpResponse
from queryapp.models import Query
from queryapp.forms import Question
from django.shortcuts import render
from django.http import HttpResponseRedirect

import sys
sys.path.append('/home/jcoreyes/NLQA/query_engine')
import mainquery
def home(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        q = Question(request.POST)
        # check whether it's valid:
        if q.is_valid():
            # process the data in form.cleaned_data as required
            questionstring = "Question: " #+ q.cleaned_data['question'] + "\n" 
            answerstring = "Answer: " + mainquery.query(q.cleaned_data['question'])
            # redirect to a new URL:
            #render_to_response("queryapp/home.html", {'questionAsked': questionstring})

            return render_to_response("queryapp/home.html", {'answer': answerstring})

    # if a GET (or any other method) we'll create a blank form
    else:
        q = Question()

    return render(request, 'queryapp/home.html', {'form': q})
