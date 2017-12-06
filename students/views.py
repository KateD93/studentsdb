#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse


# Views for Students
def students_list(request):
    students = ({'id': 1,
                 'first_name': u'Світлана',
                 'last_name': u'Подолянчук',
                 'middle_name': u'Степанівна',
                 'ticket': 233,
                 'image': "img/Lana.jpg"
                 },
                {'id': 2,
                 'first_name': u'Наталя',
                 'last_name': u'Клюха',
                 'middle_name': u'Володимирівна',
                 'ticket': 256,
                 'image': "img/Nata.jpg"
                 },
                {'id': 3,
                 'first_name': u'Максим',
                 'last_name': u'Девда',
                 'middle_name': u'Петрович',
                 'ticket': 248,
                 'image': "img/Max.jpg"
                 },
                {'id': 4,
                 'first_name': u'Катерина',
                 'last_name': u'Денищич',
                 'middle_name': u'Василівна',
                 'ticket': 223,
                 'image': "img/Kate.jpg"},
                )
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


# Views for Groups
def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
