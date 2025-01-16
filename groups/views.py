from django.shortcuts import render, get_object_or_404, redirect
from .models import Group
from django.db import IntegrityError
from teachers.models import Teacher
from students.models import Student


def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/groups-list.html', ctx)

def group_create(request):
    teachers = Teacher.objects.all()
    students = Student.objects.all()

    if request.method == 'POST':
        class_leader = request.POST.get('class_leader')
        group_name = request.POST.get('group_name')
        student_ids = request.POST.getlist('students')

        if group_name:
            teacher = Teacher.objects.get(pk=class_leader)
            group = Group.objects.create(
                class_leader=teacher,
                group_name=group_name,
            )
            if student_ids:
                group.students.set(student_ids)
            return redirect('groups:group_list')

    ctx = {
        'teachers': teachers,
        'students': students
    }
    return render(request, 'groups/group-add.html', ctx)

def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    teachers = Teacher.objects.all()
    students = Student.objects.all()

    if request.method == 'POST':
        class_leader_id = request.POST.get('class_leader')
        group_name = request.POST.get('group_name')
        student_ids = request.POST.getlist('students')

        if class_leader_id and group_name:
            class_leader = Teacher.objects.get(pk=class_leader_id)
            group.class_leader = class_leader
            group.group_name = group_name
            if student_ids:
                group.students.set(student_ids)
            group.save()
            return redirect(group.get_detail_url())

    ctx = {
        'group': group,
        'teachers': teachers,
        'students': students
    }
    return render(request, 'groups/group-add.html', ctx)


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    ctx = {'group': group}
    return render(request, 'groups/group-detail.html', ctx)


def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect('groups:group_list')

