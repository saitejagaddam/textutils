# I have created this file.
from django.http import HttpResponse
from django.shortcuts import render

# Code for video 6
# def index(request):
#     return HttpResponse("<h1>Hello Folks</h1>")
#
# def about(request):
#     return HttpResponse("About Folks")

# Code for video 7
def index(request):
    # params = {'name': 'Indian', 'place': 'India'}
    return render(request, 'index.html'#,params
    )
    # return HttpResponse("Home")

def ex1(request):
    s = '''
        <h2>
            Official links to the respective websites.
        </h2>
        <br>
        <a href = "https://www.youtube.com/" target = "_blank">Youtube</a>
        <br>
        <a href = "https://www.facebook.com/" target = "_blank">Facebook</a>
        <br>
        <a href = "https://www.gmail.com/" target = "_blank">Gmail</a>
        <br>
        <a href = "https://www.google.com/" target = "_blank">Google</a>
        '''
    return HttpResponse(s)

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    # print(djtext)
    # print(removepunc)

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

# def capfirst(request):
#     return HttpResponse("Capitalize First")
#
# def newlineremove(request):
#     return HttpResponse("New Line Remove")
#
# def spaceremover(request):
#     return HttpResponse("Space Remover <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("Character Count")
