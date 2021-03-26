from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.utils import timezone
from .models import Todo
def page(request):
    return render(request,'todo/index.html')
@csrf_exempt
def add_todo(request):
    print(request.POST)
    added_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    return render(request,'todo/index.html')
