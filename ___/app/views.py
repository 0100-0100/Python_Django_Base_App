from django.shortcuts import render

# Create your views here.


def view(request):
    """Empty Django view."""
    return render(request, 'template.html', {})
