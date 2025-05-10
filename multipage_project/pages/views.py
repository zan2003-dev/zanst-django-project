from django.shortcuts import render

def page1(request):
    return render(request, 'pages/page1.html', {'title': 'Page 1'})

def page2(request):
    return render(request, 'pages/page2.html', {'title': 'Page 2'})

def page3(request):
    return render(request, 'pages/page3.html', {'title': 'Page 3'})

def page4(request):
    return render(request, 'pages/page4.html', {'title': 'Page 4'})

def page5(request):
    return render(request, 'pages/page5.html', {'title': 'Page 5'})