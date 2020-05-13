from django.shortcuts import render
from django.http import HttpResponse
def samplehtml(request):
    return render(request, "sample.html")
def aboutus(request):
    return render(request, "aboutus.html")
def countpage(request):
    text = request.GET['matter']
    words = len(text.split())
    l = text.split()
    ll = list(set(l))
    l3 = []
    for i in ll:
        count = 0
        for j in range(len(l)):
            if i == l[j]:
                count = count + 1
        l3.append((i, count))
    d = dict(l3)
    print(words)
    return render(request, "countpage.html", {"msg":text, "length":words, "dictionary":d})