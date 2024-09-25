from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import NewsModel,AppointmentModel,ContactModel
from .forms import NewsForm,AppointmentForm,ContactForm
from django.shortcuts import get_object_or_404

# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.success(request, ("There Was An Error Loging In, Try Again..."))
            return redirect('login')
    return render(request, 'authenticate/login.html')

@login_required(login_url='user_login')
def admin_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'admin_dashboard.html')
    else:
        return redirect('user_login')

def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('index')

def index(request):
    news = NewsModel.objects.all()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = AppointmentForm()
    return render(request, 'index.html', {'form': form,'news':news})

@login_required(login_url='user_login')
def appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        phone = request.POST['phone']
        place = request.POST['city']
        state = request.POST['state']
        date = request.POST['date']
        data = AppointmentModel(name=name,age=age,phone=phone,place=place,state=state,date=date)
        data.save()
        return HttpResponseRedirect('admin_appointment_view')
    return render(request,'index.html')

@login_required(login_url='user_login')
def admin_appointment_view(request):
    appointment = AppointmentModel.objects.all()
    return render(request, 'admin_appointment_view.html', {'appointment': appointment})

@login_required(login_url='user_login')
def admin_delete_appointments(request,id):
    appointment = AppointmentModel.objects.get(id=id)
    appointment.delete()
    return redirect('admin_appointment_view')

@login_required(login_url='user_login')
def admin_add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('admin_news_view') 
    else:
        form = NewsForm()

    return render(request, 'admin_add_news.html', {'form': form})

@login_required(login_url='user_login')
def admin_news_view(request):
    news = NewsModel.objects.all()
    return render(request, 'admin_news_view.html', {'news': news})

@login_required(login_url='user_login')
def admin_update_news(request,id):
    news = get_object_or_404(NewsModel, id=id)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            return redirect('admin_news_view')
    else:
        form = NewsForm(instance=news)
    return render(request, 'admin_update_news.html', {'form': form, 'news': news})

@login_required(login_url='user_login')
def admin_delete_news(request,id):
    news = NewsModel.objects.get(id=id)
    news.delete()
    return redirect('admin_news_view')




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('contact') 
    else:
        form = ContactForm()

    return render(request,'contact.html',{'form':form})

@login_required(login_url='user_login')
def admin_contact_view(request):
    contact = ContactModel.objects.all()
    return render(request,'admin_contact_view.html',{'contact':contact})


@login_required(login_url='user_login')
def admin_delete_contact(request,id):
    contact = ContactModel.objects.get(id=id)
    contact.delete()
    return redirect('admin_contact_view')

def disorders_of_women(request):
    return render(request,'disorders_of_women.html')

def skin_disorders(request):
    return render(request,'skin_disorders.html')

def cardiac_disorders(request):
    return render(request,'cardiac_disorders.html')


def doctor_profile(request):
    return render(request,'doctor_profile.html')

def home(request):
    return render(request,'index-2.html')





