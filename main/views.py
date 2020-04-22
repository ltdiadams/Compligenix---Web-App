# from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
# from .models import Post
# from django.urls import reverse
# from django.views.generic.edit import FormView
# from .forms import HomeForm

# Create your views here.
# def first(request):
#     return render(request, 'index.html')

# class FormView1(FormView):
#     template_name = 'index.html'
#     # form_class = RequiredInputsForm
#     # success_url = '/index/success/'
#
#     def get(self, request):
#         form = HomeForm()
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = HomeForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()
#
#             phone = form.cleaned_data['post']
#             form = HomeForm()
#             return redirect('index:index')
#
#             args = {'form': form, 'text': text}
#             return render(request, self.template_name, args)


# def insert_my_num(request: HttpRequest):
#     phone = Post(content=request.POST['content'])
#     phone.save()
#     return redirect('')

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.core.exceptions import ValidationError
# import pymsgbox
from .models import Todo
from .forms import Post

from twilio.rest import Client
# Create your views here.

# codes required by twilio. These are specific to the twilio account being used.
account_sid = 'AC4141b76e99a2898f4f535c7e026a37ab'
auth_token = '9bccc5fc4f1105e4c12bb1e9e99fc4a4'

client = Client(account_sid, auth_token)

sender = '+12052728434'

def list_todo_items(request):
    context = {
        'todo_list' : Todo.objects.all(),
        'count': Todo.objects.count()
    }
    # count = Todo.objects.count()
    # context2 = {'count': count}
    # context = {'count': Todo.objects.count()}
    # count = Todo.objects.count()
    return render(request, 'index.html', context)

# use twilio to send message to the inputted number!
# probably don't need to access the database at all :)
# want to send to todo.objects.
def insert_todo_item(request: HttpRequest):
    todo = Todo(content=request.POST['content'])
    try:
        todo.full_clean()

    except ValidationError:
        # pymsgbox.alert('ValidationError! Phone number must be entered in the format: +999999999. Up to 15 digits allowed.', 'Title')
        return redirect('/main/list/')

    todo.save()
    # reciever = '+15063270183' #WORKSSSSSSSS
    reciever = Todo.objects.values_list('content', flat=True).distinct()
    # reciever = Todo.objects.filter

    text = 'You are awesome!'
    client.messages.create(to=reciever, from_=sender, body=text)


    return redirect('/main/list/')

def delete_todo_item(request,todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/main/list/')