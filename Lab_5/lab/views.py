from django.shortcuts import render , redirect
from .models import Person, people


def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_person = Person(username, password)
        people.append(new_person)
        return redirect('default')
    return render(request, 'lab/templates/lab5/add.html')

def default_view(request):
    return render(request, 'lab/templates/lab5/default.html', {'people': people})


