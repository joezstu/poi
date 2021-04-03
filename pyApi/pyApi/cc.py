from django.shortcuts import render


def bc(request):
    return render(request, 'test.html')
