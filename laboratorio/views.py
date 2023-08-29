from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LaboratorioForm
from laboratorio.models import Laboratorio

# Create your views here.
def v_list(request):
    consulta = Laboratorio.objects.all()

    # if 'num_visits' in request.session:
    #     num = request.session['num_visits']
    # else:
    #     num = 0
    # request.session['num_visits'] = num + 1
    # num_visits = request.session['num_visits']

    "#Number of visits to this view, as counted in the session variable."
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {'laboratorios': consulta, 'num_visits': num_visits}
    return render(request, 'list.html', context)

def v_create(request):
    if request.method == 'POST':
        datos = request.POST.copy()
        formcrear = LaboratorioForm(datos)
        if formcrear.is_valid():
            formcrear.save()
            return HttpResponseRedirect('/')

    context = {
        'formulario': LaboratorioForm()
    }
    return render(request, 'create.html', context)

def v_update(request, laboratorio_id):
    lab = Laboratorio.objects.get(id = laboratorio_id)

    if request.method == 'POST':
        datos = request.POST.copy()
        formeditar = LaboratorioForm(datos, instance = lab)
        if formeditar.is_valid():
            formeditar.save()
        return HttpResponseRedirect('/')
    else:
        context = {
            'formedicion': LaboratorioForm(instance = lab)
        }
        return render(request, 'update.html', context)

def v_delete(request, laboratorio_id):
    if request.method == 'POST':
        from .models import Producto, DirectorGeneral
        Producto.objects.filter(laboratorio = laboratorio_id).delete()
        DirectorGeneral.objects.filter(laboratorio = laboratorio_id).delete()
        Laboratorio.objects.get(id = laboratorio_id).delete()
        return HttpResponseRedirect('/')

    context = {
        'lab': Laboratorio.objects.get(id = laboratorio_id)
    }
    return render(request, 'delete.html', context)