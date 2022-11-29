
from email import message
from django.shortcuts import redirect, render

from home.form import BookingForm
from .models import contactus, departments, doc
# Create your views here.
def index(request):
    #return(HttpResponse("Home page"))
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirm.html')

    form = BookingForm()
    dict_form = {
        'form' : form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    dict_docs = {
        'docs' : doc.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def contact(request):
    if request.method == 'POST':
        new_msg = contactus(
            c_name = request.POST['fullname'],
            c_email = request.POST['mail'],
            c_msg = request.POST['mesg']
        )
        new_msg.save()
        return render(request,'msgconfirm.html')
    return render(request,'contact.html')
def department(request):
    dict_dept={
        'dept': departments.objects.all()
    }
    return render(request,'department.html',dict_dept)
    