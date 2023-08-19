from django.shortcuts import render
from django.http import HttpResponseRedirect
from laboratorio.models import Laboratorio

# Create your views here.
def v_list(request):
    consulta = Laboratorio.objects.all()
    
    "#Number of visits to this view, as counted in the session variable."
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {'laboratorios': consulta, 'num_visits': num_visits}
    return render(request, 'list.html', context)

def v_create(request):
    context = {}
    return render(request, 'create.html', context)

def v_update(request, laboratorio_id):
    consulta = Laboratorio.objects.all()
    context = {'laboratorio': consulta }
    return render(request, 'update.html', context)

def v_delete(request, laboratorio_id):
    if request.method == 'POST':
        Laboratorio.objects.filter(id=laboratorio_id).delete()
        return HttpResponseRedirect("/")
    return render(request, 'delete.html', context)