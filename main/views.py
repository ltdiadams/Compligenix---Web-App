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
# Create your views here.


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


def insert_todo_item(request: HttpRequest):
    todo = Todo(content=request.POST['content'])
    try:
        todo.full_clean()

    except ValidationError:
        # pymsgbox.alert('ValidationError! Phone number must be entered in the format: +999999999. Up to 15 digits allowed.', 'Title')
        return redirect('/main/list/')

    todo.save()
    return redirect('/main/list/')

def delete_todo_item(request,todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/main/list/')