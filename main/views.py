from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import ValidationError
# import pymsgbox
from .models import Phone
from .forms import Post
import subprocess
# import threading
import time
# from django_simple_task import defer

from twilio.rest import Client
# Create your views here.

# codes required by twilio. These are specific to the twilio account being used.
account_sid = 'AC4141b76e99a2898f4f535c7e026a37ab'
auth_token = 'bb4932b69d68ee4aca772d6ed685460c'


    # will just keep running in the background
    # while users request compliments, means some may get the same
    # compliment until the next compliment is written, so there is
    # about a 30 second window for two of the same compliments.
    # alternative was to implement a queueing system with background
    # task, this is much simpler and will do the trick for app's purpose



client = Client(account_sid, auth_token)

sender = '+12052728434'

def list_phone_items(request):
    context = {
        'phone_list' : Phone.objects.all(),
        'count': Phone.objects.count()
    }

    return render(request, 'index.html', context)

# use twilio to send message to the inputted number!
# probably don't need to access the database at all :)
# want to send to todo.objects.

def insert_phone_item(request: HttpRequest):
    phone = Phone(content=request.POST['content'])
    try:
        phone.full_clean()

    except ValidationError:
        # pymsgbox.alert('ValidationError! Phone number must be entered in the format: +999999999. Up to 15 digits allowed.', 'Title')
        return redirect('/')

    phone.save()

    # reciever = '+15063270183' #WORKSSSSSSSS
    reciever = Phone.objects.values_list('content', flat=True).order_by('-id')[0]#.distinct()
    # reciever = Todo.objects.filter
    # defer(task)
    subprocess.Popen(["python", "create_model.py"]) # runs create_model code but the rest of the app proceeds without it

    with open('textgenrnn_texts.txt', 'r') as myfile:
        text = myfile.read()

    # text = "Yoooo"
    client.messages.create(to=reciever, from_=sender, body= text)

    # use django background tasks!!!!!!! https://django-background-tasks.readthedocs.io/en/latest/
    # to make the texts daily, etc.

    return redirect('/')

def delete_phone_item(request,phone_id):
    todo_to_delete = Phone.objects.get(id=phone_id)
    todo_to_delete.delete()
    return redirect('/')

#---------------------------------------------------------------------------------------------
# NOTE TO SELF: multithreading is NOT the solution, created an unkillable process
# that just kept trying to write compliments non stop

# it was also laggy as shit.

# b = threading.Thread(name='write_compliments_loop', target=write_compliments_loop)
# f = threading.Thread(name='insert_phone_item', target=insert_phone_item)

# b.start()
# f.start()