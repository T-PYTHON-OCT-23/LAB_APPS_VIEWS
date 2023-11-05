from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World, This is my new HOME for Car Rentals Website! We're excited to welcome you here.")



def info(request):
    content='''
    
    <!DOCTYPE html>
<html>
<head>
    <title>About Cars</title>
</head>
<body>
    <p>When it comes to automobiles, cars have revolutionized the way we live and travel. They offer us the freedom to explore the world, commute to work, and go on exciting road trips. Cars come in various shapes, sizes, and styles, catering to diverse needs and preferences. Whether you're interested in eco-friendly electric cars, powerful sports cars, or practical family vehicles, there's a car for everyone. With advanced technologies and safety features, modern cars make our journeys more comfortable and secure. The automotive industry continues to innovate, making cars an integral part of our daily lives.</p>
</body>
</html>

    
    
    '''
    return HttpResponse(content)
