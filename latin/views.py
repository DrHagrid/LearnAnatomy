# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render
from latin.models import element_types, element_groups
from users.models import UserInfo
import random


# Проверка ответа
def check_answer(request):
    return_dict = dict()
    data = request.POST
    answer = data.get("answer")
    element_group = data.get("element_group")
    element_type = data.get("element_type")
    element_id = data.get("element_id")
    element = element_groups.get(element_group).objects.get(pk=element_id)
    start = data.get("start")

    replica_success = random.choice([
        'Вы ответили верно! Поздравляю!',
        'Верно!',
        'Вы ответили правильно. Продолжайте дальше!'
    ])
    replica_fail = random.choice([
        'Ответ не верный. Попробуйте ещё.',
        'Ответ не верный. Нажмите "Подсказка", если хотите посмотреть ответ.',
        'Не верно!'
    ])

    return_dict["response"] = False
    initial = element.name_lat.lower().split(' ')
    entrance = answer.lower().split(' ')
    intersection = list(set(initial) & set(entrance))

    return_dict["replica_success"] = replica_success
    return_dict["replica_fail"] = replica_fail

    if (len(entrance) == len(initial)) and (len(entrance) == len(intersection)):  # При условии верного ответа
        group_class = element_groups.get(element_group)
        type_class = element_types.get(element_group).objects.get(variable=element_type)
        elements_selection = group_class.objects.filter(type=type_class)
        elements_id = list()
        for e in elements_selection:
            elements_id.append(e.id)
        elements_id.sort()
        for e in elements_id:
            if e > int(element_id):
                next_element_id = e
                break
            else:
                next_element_id = 0

        response = 'True'

        return_dict["element_group"] = element_group
        return_dict["element_type"] = element_type
        return_dict["next_element_id"] = next_element_id
        return_dict["name_lat"] = element.name_lat
        return_dict["info"] = element.info
    else:
        response = 'False'

    # Если пользователь зарегистрирован, то сохранить статистику
    if request.user.is_authenticated:
        user_info = UserInfo.objects.get(user=request.user)

        if user_info.data:
            user_data = user_info.get_data()
        else:
            user_data = dict()

        if response == 'True':
            if start == 'True':
                user_data[element_group + "_" + element_type] = {'correct': 0, 'incorrect': 0, 'hint': 0}
                user_data[element_group + "_" + element_type]['correct'] += 1
        else:
            if start == 'True':
                user_data[element_group + "_" + element_type] = {'correct': 0, 'incorrect': 0, 'hint': 0}
            user_data[element_group + "_" + element_type]['incorrect'] += 1
        user_info.set_data(user_data)
        user_info.save(force_update=True)

    return_dict["response"] = response

    return JsonResponse(return_dict)


# Страница выбора группы элементов
def test_choice_group(request):

    return render(request, 'latin/test_choice_group.html', locals())


# Страница выбора отдела
def test_choice_type(request, element_group):
    class_name = element_groups.get(element_group).class_name  # Название отдела
    types = element_types.get(element_group).objects.all()  # Список с типами анатомических элементов

    # Если пользователь зарегистрирован, то получить user_data
    if request.user.is_authenticated:
        user_info = UserInfo.objects.get(user=request.user)
        if user_info.data:
            user_data = user_info.get_data()
        else:
            user_data = dict()

    total = list()  # Список с типами анатомических элементов

    for type in types:
        # Если пользователь зарегистрирован, то загрузить/создать статистику
        if request.user.is_authenticated:
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
        else:
            total.append({"type": type, "status": 'none'})

    return render(request, 'latin/test_choice_type.html', locals())


# Страница теста
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

    return render(request, 'latin/test.html', locals())


# Страница статистики
def stat(request, element_group, element_type):
    group_class = element_groups.get(element_group)
    type_class = element_types.get(element_group).objects.get(variable=element_type)

    # Если пользователь зарегистрирован, то загрузить статистику
    if request.user.is_authenticated:
        user_info = UserInfo.objects.get(user=request.user)
        user_data = user_info.get_data()
        correct = user_data[element_group + "_" + element_type]['correct']
        incorrect = user_data[element_group + "_" + element_type]['incorrect']
        hint = user_data[element_group + "_" + element_type]['hint']

    return render(request, 'latin/stat.html', locals())
