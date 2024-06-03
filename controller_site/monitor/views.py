from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import ListJobs
import datetime as dt


def index(request):
    active_tasks = ListJobs.objects.filter(active=True)
    completed_tasks = []
    print(str(request.POST))

    ls = [
        'workshop_number',
        'name_model',
        'name_order',
        'name_operation',
        'number_operation',
        'name_work_center_name',
        'full_name_of_the_workers'
    ]
    if 'workshop_number' in request.POST.keys() and request.POST['workshop_number']:
        dct = {elem: request.POST[elem] for elem in ls}
        dct['creation_date'] = dt.datetime.strptime(request.POST['creation_date_0'] + request.POST['creation_date_1']
                                                    , '%Y-%m-%d%M:%S')
        ListJobs.objects.get_or_create(
            workshop_number=dct['workshop_number'],
            creation_date=dct['creation_date'],
            name_model=dct['name_model'],
            name_order=dct['name_order'],
            name_operation=dct['name_operation'],
            number_operation=dct['number_operation'],
            name_work_center_name=dct['name_work_center_name'],
            full_name_of_the_workers=dct['full_name_of_the_workers']
        )

    return render(request, 'monitor/index.html',
                  {"active_tasks": active_tasks, 'completed_tasks': completed_tasks})


def created_task(request):
    return render(request, 'monitor/created_task.html')
