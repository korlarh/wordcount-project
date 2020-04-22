from django.http import HttpResponse
from django.shortcuts import render
import operator

def index(request):
    return render(request, 'home.htm')


def count(request):
    fulltext = request.GET['fulltext']
    wordcount = fulltext.split()

    worddictionary = {}

    for word in wordcount:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse= True)

    return render(request, 'count.htm', {'ft':fulltext, 'wc':len(wordcount), 'sortedwords':sortedwords})


def about(request):
    return render(request, 'about.htm')
