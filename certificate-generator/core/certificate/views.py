from django.shortcuts import render
from .models import Certificate
import os
from django.conf import settings
from django.http import HttpResponse, FileResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from PIL import Image, ImageDraw, ImageFont

# Create your views here.
def index(request):
    certificate = Certificate.objects.all()
    context = {
        'certificate': certificate,
    }
    return render(request, 'certificate/index.html', context)

def certificate(request, pk):
    certificate = Certificate.objects.get(id=pk)
    event=certificate.event
    name=certificate.name
    print(f'static/images/events/{certificate.gender.lower()}_{certificate.event.lower()}.jpg')
    
    image = Image.open(f'static/images/events/{certificate.gender.lower()}_{certificate.event.lower()}.jpg')
    
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.truetype("Roboto-BoldItalic.ttf", 30)
    
    # starting position of the message
    
    (x, y) = (221, 680)
    distance = f'{certificate.kilometers} KM'
    color = 'rgb(23, 63, 63)' # black color
    
    # draw the message on the background
    
    draw.text((x, y), distance, fill=color, font=font)

    (x, y) = (810, 680)
    time = f'{certificate.hours} Hours'
    color = 'rgb(23, 63, 63)' # white color
    draw.text((x, y), time, fill=color, font=font)

    font = ImageFont.truetype("Roboto-Bold.ttf", 60)

    # (x,y) = (460,510)
    (X,Y) = (1280,510)
    name = certificate.name
    x,y = draw.textsize(name)
    # print((X-x)/2)
    color = 'rgb(23, 63, 63)'
    draw.text(((X-5*x)/2, Y), name, fill=color, font=font)
    
    # save the edited image
    
    image.save(f'static/images/certificates/{certificate.name}_{certificate.gender}_{certificate.event}.png')
    
    template_path = 'certificate/event_certificate.html'
    context = {
        'certificate': certificate
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = f'filename={name}_"Adventure_Sports_Club_IITK_Amrit_Mahotsav_{event}_Event_Participation_Certificate".pdf'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def certificateImage(request, pk):
    certificate = Certificate.objects.get(id=pk)
    event=certificate.event
    name=certificate.name
    context = {
        'certificate': certificate
    }
    # print(f'static/images/events/{certificate.gender.lower()}_{certificate.event.lower()}.jpg')
    
    image = Image.open(f'static/images/events/{certificate.gender.lower()}_{certificate.event.lower()}.jpg')
    
    draw = ImageDraw.Draw(image)
    
    font = ImageFont.truetype("Roboto-BoldItalic.ttf", 30)
    
    # starting position of the message
    
    (x, y) = (221, 680)
    distance = f'{certificate.kilometers} KM'
    color = 'rgb(23, 63, 63)' # black color
    
    # draw the message on the background
    
    draw.text((x, y), distance, fill=color, font=font)

    (x, y) = (810, 680)
    time = f'{certificate.hours} Hours'
    color = 'rgb(23, 63, 63)' # white color
    draw.text((x, y), time, fill=color, font=font)

    font = ImageFont.truetype("Roboto-Bold.ttf", 60)

    (X,Y) = (1280,510)
    name = certificate.name
    x,y = draw.textsize(name)
    # print((X-x)/2)
    color = 'rgb(23, 63, 63)'
    draw.text(((X-5*x)/2, Y), name, fill=color, font=font)
    # save the edited image
    
    image.save(f'static/images/certificates/{certificate.name}_{certificate.gender}_{certificate.event}.jpg')
    
    img = open(f'static/images/certificates/{certificate.name}_{certificate.gender}_{certificate.event}.jpg', 'rb')

    response = FileResponse(img)
    
    response['Content-Disposition'] = f'filename={name}_"Adventure_Sports_Club_IITK_Amrit_Mahotsav_{event}_Event_Participation_Certificate".jpg'

    return response
    
    # Create a Django response object, and specify content_type as pdf
    # response = HttpResponse('static/images/certificates/{certificate.name}_{certificate.gender}_{certificate.event}.png',content_type='image/png')

    # response['Content-Disposition'] = f'filename={name}_"Adventure_Sports_Club_IITK_Amrit_Mahotsav_{event}_Event_Participation_Certificate".png'
    
    # return response
    
    # return render(request, 'certificate/event_certificate.html', context)