from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import ValidationError
# import pymsgbox
from .models import Phone
from .forms import Post
import subprocess

from twilio.rest import Client
# Create your views here.

# codes required by twilio. These are specific to the twilio account being used.
account_sid = 'AC4141b76e99a2898f4f535c7e026a37ab'
auth_token = 'b19e3f45d0cf722adb26b0f643d72dce'

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
        return redirect('/main/list/')

    phone.save()
    # reciever = '+15063270183' #WORKSSSSSSSS
    reciever = Phone.objects.values_list('content', flat=True).distinct()
    # reciever = Todo.objects.filter

    subprocess.call(["python", "create_model.py"])

    with open('textgenrnn_texts.txt', 'r') as myfile:
        text = myfile.read()

    # text = "Yoooo"
    client.messages.create(to=reciever, from_=sender, body=text)


    return redirect('/main/list/')

def delete_phone_item(request,phone_id):
    todo_to_delete = Phone.objects.get(id=phone_id)
    todo_to_delete.delete()
    return redirect('/main/list/')