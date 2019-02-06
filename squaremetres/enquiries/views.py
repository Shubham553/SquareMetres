from django.shortcuts import render, redirect
from .models import Enquiry
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


# # Create your views here.
def enquiry(request):
    if request.method == 'POST':
        property_id = request.POST['property_id']
        property_name = request.POST['property_name']
        user = request.POST['user']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        dealer_id = request.POST['dealer_id']
        buyer_id = request.POST['buyer_id']
        dealer_email = request.POST['dealer_email']

        #  Check if user has made enquiry already
        if request.user.is_authenticated:
            has_contacted = Enquiry.objects.all().filter(property_id=property_id, buyer_id=buyer_id)

            if has_contacted:
                messages.error(request, 'You have already made an enquiry for this property')
                return redirect('/property/'+str(property_id))

        enquire = Enquiry(property_name=property_name, property_id=property_id, user=user, email=email, phone=phone,
                          message=message, dealer_id=dealer_id, buyer_id=buyer_id)
        enquire.save()

        subject, from_email, to = 'ENQUIRY LISTED', settings.EMAIL_HOST_USER, dealer_email
        text_content = 'A Buyer has made an enquiry for your posted property.'
        url = "http://127.0.0.1:8000/property/{}/".format(property_id)
        html_content = '<p><strong>Alert</strong> message.</p><br><p>A Buyer has made an enquiry for ' \
                       'your posted property.</p> <br> <strong>{}</strong> having email id <strong>{}</strong> and ' \
                       'phone number <strong>{}</strong> is interseted in your property name<a href={}> {} </a>.' \
                       ' <br> please login and check for more details. <br>Thanks. <br> Team <strong>TOTHENEW.<strong>'\
            .format(user, email, phone, url, property_name)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        messages.success(request, 'Thanks for submitting enquiry, a Dealer will get back to you soon')

    return redirect('/')


def enquiries(request):
    enquire = Enquiry.objects.order_by('-enquiry_date').filter(dealer_id=request.user.id)

    return render(request, 'enquiry.html', {'enquiries': enquire})
