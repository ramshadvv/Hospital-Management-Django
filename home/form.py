from dataclasses import fields
from django import forms
from home.models import bookings
class DateInput(forms.DateInput):
    input_type = 'date'
class BookingForm(forms.ModelForm):
    class Meta:
        model = bookings
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput()
        }
        labels = {
            'p_name' : "PATIENT NAME",
            'p_phone': "PATIENT PHONE",
            'p_email': "EMAIL", 
            'doc_name': "DOCTOR NAME",
            'booking_date': "BOOKING DATE"
        }