from django.shortcuts import render
from content.models import Bone, BoneType
from content.models import element_types, element_groups


def info_choice(request):
    types = BoneType.objects.all()
    return render(request, 'info_choice.html', locals())


def info(request, type_variable):
    bone_type = BoneType.objects.get(variable=type_variable)
    bones = Bone.objects.filter(type=bone_type)
    return render(request, 'info.html', locals())


def test_choice_group(request):
    return render(request, 'test_choice_group.html', locals())


def test_choice_type(request, element_group):
    types = element_types.get(element_group).objects.all()
    return render(request, 'test_choice_type.html', locals())


def test(request, element_group, element_type, element_id):
    group_class = element_groups.get(element_group)
    type_class = element_types.get(element_group).objects.get(variable=element_type)
    if element_id == 'undefined':
        elements_selection = group_class.objects.filter(type=type_class)
        elements_id = list()
        for e in elements_selection:
            elements_id.append(e.id)
        elements_id.sort()
        element_id = elements_id[0]
        print(element_id)
    element = group_class.objects.get(pk=element_id)
    return render(request, 'test.html', locals())


def stat(request, element_group, element_type):
    group_class = element_groups.get(element_group)
    type_class = element_types.get(element_group)
    return render(request, 'stat.html', locals())
