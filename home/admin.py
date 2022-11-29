from django.contrib import admin
from .models import bookings, contactus, departments, doc
# Register your models here.
admin.site.register(departments)
admin.site.register(doc)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','c_name','c_email','c_msg','msg_on')
admin.site.register(contactus, ContactAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on')
admin.site.register(bookings, BookingAdmin)