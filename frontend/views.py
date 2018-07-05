from django.shortcuts import render
from content.models import Bone, BoneType
from content.models import element_types, element_groups
from users.models import UserInfo


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
    class_name = element_groups.get(element_group).class_name
    types = element_types.get(element_group).objects.all()
    user_info = UserInfo.objects.get(user=request.user)
    if user_info.data:
        user_data = user_info.get_data()
    else:
        user_data = dict()
    total = list()
    for type in types:
        if element_group + "_" + type.variable in user_data.keys():
            e = user_data[element_group + "_" + type.variable]
        else:
            user_data[element_group + "_" + type.variable] = {'correct': 0, 'incorrect': 0, 'hint': 0}
            user_info.set_data(user_data)
            user_info.save(force_update=True)
            e = user_data[element_group + "_" + type.variable]
        if e['correct'] == 0 and e['incorrect'] == 0:
            status = 'none'
        elif e['incorrect'] == 0 and e['correct'] > 0:
            status = 'excellent'
        elif e['correct'] > e['incorrect']:
            status = 'good'
        else:
            status = 'bad'
        total.append({"type": type, "status": status})
    return render(request, 'test_choice_type.html', locals())


def test(request, element_group, element_type, element_id):
    group_class = element_groups.get(element_group)
    type_class = element_types.get(element_group).objects.get(variable=element_type)
    if element_id == 'undefined':
        start = True
        elements_selection = group_class.objects.filter(type=type_class)
        elements_id = list()
        for e in elements_selection:
            elements_id.append(e.id)
        elements_id.sort()
        element_id = elements_id[0]
    element = group_class.objects.get(pk=element_id)
    return render(request, 'test.html', locals())


def stat(request, element_group, element_type):
    group_class = element_groups.get(element_group)
    type_class = element_types.get(element_group).objects.get(variable=element_type)
    return render(request, 'stat.html', locals())
