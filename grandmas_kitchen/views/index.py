# from django.http import HttpResponse
# import datetime

# def index(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

from django.shortcuts import render, redirect
# from .get_jobs import get_jobs


def index(request):
	template = 'grandmas_kitchen/home.html'
	if request.user.is_authenticated:
		return render(request, template)
	else:
		return redirect('login')