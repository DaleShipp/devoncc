from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic

from rallybooking.models import Rally


def index(request):
    rally_list = Rally.objects.order_by('-start_date')[:5]
    template = loader.get_template('rallybooking/index.html')
    context = {
        'rally_list': rally_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, rally_id):
    try:
        rally = Rally.objects.get(pk=rally_id)
    except Rally.DoesNotExist:
        raise Http404("Rally does not exist")
    return render(request, 'rallybooking/detail.html', {'rally': rally})

def results(request, rally_id):
    response = "You're looking at the results of rally %s."
    return HttpResponse(response % rally_id)

def publish(request, rally_id):
    return HttpResponse("You're publishing on rally %s." % rally_id)


class IndexView(generic.ListView):
    template_name = 'rallybooking/index.html'
    context_object_name = 'rally_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Rally.objects.order_by('-start_date')



class DetailView(generic.DetailView):
    model = Rally
    template_name = 'rallybooking/detail.html'