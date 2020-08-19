from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#admin home
@login_required
def home(request):
    employeelist = User.objects.all()
    context = {
        'employeelist':employeelist,
    }
    return render(request, 'home.html', context)