# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .models import Member, FinanceOfficer

# # Create your views here.
# def index(request): 
# 	return render(request, 'index.html') 

# @login_required
# def member_dashboard(request):
#     if not request.user.groups.filter(name='Members').exists():
#         return redirect('login')
#     member = Member.objects.get(email=request.user.email)
#     return render(request, 'member_dashboard.html', {'member': member})

# @login_required
# def finance_officer_dashboard(request):
#     if not request.user.groups.filter(name='Finance Officers').exists():
#         return redirect('login')
#     finance_officer = FinanceOfficer.objects.get(email=request.user.email)
#     return render(request, 'finance_officer_dashboard.html', {'finance_officer': finance_officer})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Member, FinanceOfficer

# Existing views

def index(request): 
	return render(request, 'index.html') 

@login_required
def member_dashboard(request):
    if not request.user.groups.filter(name='Members').exists():
        return redirect('login')
    member = Member.objects.get(email=request.user.email)
    return render(request, 'member_dashboard.html', {'member': member})

@login_required
def finance_officer_dashboard(request):
    if not request.user.groups.filter(name='Finance Officers').exists():
        return redirect('login')
    finance_officer = FinanceOfficer.objects.get(email=request.user.email)
    return render(request, 'finance_officer_dashboard.html', {'finance_officer': finance_officer})

def loginUser(request):
    return render(request, 'login_page.html')

def doLogin(request):
    if request.method == 'POST':
        email_id = request.POST.get('email')
        password = request.POST.get('password')

        if not (email_id and password):
            messages.error(request, "Please provide all the details!")
            return render(request, 'login_page.html')

        user = authenticate(request, email=email_id, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'member'):
                return redirect('member_dashboard')
            elif hasattr(user, 'financeofficer'):
                return redirect('finance_officer_dashboard')
            else:
                messages.error(request, 'Invalid user type!')
                return render(request, 'login_page.html')
        else:
            messages.error(request, 'Invalid login credentials!')
            return render(request, 'login_page.html')
    else:
        return render(request, 'login_page.html')
    

    # Additional views for handling specific functionalities can be created similarly.
