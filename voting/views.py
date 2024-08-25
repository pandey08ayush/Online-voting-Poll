from django.shortcuts import render,redirect
from.models import Registration
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.http import Http404

from .models import Question, Choice

# Get questions and display those questions
def show_index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'app/polls/index.html', context)

# Show question and choices 
def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')
    return render(request, 'app/polls/detail.html', 
                    {'question': question})

#Get question and display results
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'app/polls/results.html',{'question':question})

# Vote for a qerstion choice
def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'app/polls/detail.html', 
                      { 'question': question,
                        'error_message': 'You did not select a choice.'})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args = (question.id,)))
    
def main(request):
     return render(request,'app/main/mainpage.html')
    

def index(request):
    return render(request, 'app/home.html')


def login(request):
    context = {
        'GENDER_CHOICES': Registration.GENDER_CHOICES,
        'STATES_CHOICES': Registration.STATES_CHOICES,
    }
    if request.method == 'POST':
        req = request.POST
        formdata = {
            'Full_Name': req.get('Full_Name'),
            'Email_address':req.get( 'Email_address'),
            'Phone_number':req.get('Phone_number'),
            'dob':req.get('dob'),
            'Gender':req.get('Gender'),
            'Street_address':req.get('Street_address'),
            'state': req.get('state'),
            'City':req.get('City'),
            'Age':req.get('Age'),
        }
        context={**context, **formdata}

#         user
# Full_Name
# Email_address
# Phone_number
# Gender
# Street_address
# state
# City
# Age
# dob
        # //usr= request.user
        candidate_ins = Registration.objects.create(
                Full_Name=formdata['Full_Name'],
                Email_address=formdata['Email_address'],
                Phone_number=formdata['Phone_number'],
                dob=formdata['dob'],
                Gender=formdata['Gender'],
                Street_address=formdata['Street_address'],
                state=formdata['state'],
                City=formdata['City'],
                Age=formdata['Age'],
        )
        try:
                candidate_ins.save()
                messages.success(request, "Submited Successfully.")
                return redirect('show_index') 

        except:
                messages.error(request, "Something Went Wrong.")
    return render(request, 'app/registration.html',context)
