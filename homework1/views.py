from django.shortcuts import render
def post_list(request):
    return render(request, 'homework1/post_list.html', {})
# Create your views here.
