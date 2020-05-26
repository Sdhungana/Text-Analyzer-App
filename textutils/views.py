from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text from the textbox
    djtext = request.POST.get('comment','default')
    # Get the checkbox value i.e. 'On' or 'Off'
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    lineremover = request.POST.get('lineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    # Punctuation Remover
    if removepunc == "on":
        punctuation_list = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
           if char not in punctuation_list:
               analyzed += char
        context = {'msg': 'Punctuation Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', context)

    # Change to Uppercase block
    if fullcaps == "on":
        analyzed = djtext.upper()
        context = {'msg': 'Changed To Uppercase','analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html',context)

    # New Line Remover
    if lineremover == "on":
        analyzed = ""
        for char in djtext:
         # /r is a carriage return which moves  the cursor back to the start of a new line
           if char != "\n" and char != "\r":  
               analyzed += char
        context = {'msg': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', context)

     # Space Remover
    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
           if not(djtext[index] == " " and djtext[index+1] == " "):
               analyzed += char
        print(analyzed)
        context = {'msg': 'Space Removed', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', context)
 
    if(removepunc !="on" and fullcaps !="on" and lineremover !="on" and spaceremover !="on"):
        return HttpResponse('<h1>Please select the option!!</h1>')
    return render(request, 'analyze.html', context)
  
