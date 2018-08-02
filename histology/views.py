# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render
from histology.models import Sample, SampleType
from users.models import UserInfo
import random


# Проверка ответа
def histology_check(request):
    return_dict = dict()
    data = request.POST
    answer = data.get("answer")
    element_type = data.get("element_type")
    element_id = data.get("element_id")
    start = data.get("start")
    element = Sample.objects.get(pk=element_id)

    replica_success = random.choice([
        'Вы ответили верно! Поздравляю!',
        'Верно!',
        'Вы ответили правильно. Продолжайте дальше!'
    ])
    replica_fail = random.choice([
        'Ответ не верный. Попробуйте ещё.',
        'Не правильно!',
        'Не верно!'
    ])

    return_dict["replica_success"] = replica_success
    return_dict["replica_fail"] = replica_fail

    if answer == "correct":  # При условии верного ответа
        type_class = SampleType.objects.get(variable=element_type)
        elements_selection = Sample.objects.filter(type=type_class)
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

        return_dict["element_type"] = element_type
        return_dict["next_element_id"] = next_element_id
        return_dict["correct_option"] = element.correct_option
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
                user_data["histology" + "_" + element_type] = {'correct': 0, 'incorrect': 0, 'incorrect_list': []}
            user_data["histology" + "_" + element_type]['correct'] += 1
        else:
            if start == 'True':
                user_data["histology" + "_" + element_type] = {'correct': 0, 'incorrect': 0, 'incorrect_list': []}
            user_data["histology" + "_" + element_type]['incorrect'] += 1
            if not any(element_id in el for el in user_data["histology" + "_" + element_type]['incorrect_list']):
                user_data["histology" + "_" + element_type]['incorrect_list'].append(element_id)
        user_info.set_data(user_data)
        user_info.save(force_update=True)

    return_dict["response"] = response

    return JsonResponse(return_dict)


# Страница выбора отдела
def histology_choice_type(request):
    types = SampleType.objects.all()  # Список с типами анатомических элементов

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
            if "histology" + "_" + type.variable in user_data.keys():
                e = user_data["histology" + "_" + type.variable]
            else:
                user_data["histology" + "_" + type.variable] = {'correct': 0, 'incorrect': 0, 'incorrect_list': []}
                user_info.set_data(user_data)
                user_info.save(force_update=True)
                e = user_data["histology" + "_" + type.variable]
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

    return render(request, 'histology/test_choice_type.html', locals())


# Страница теста
def histology(request, element_type, element_id):
    type_class = SampleType.objects.get(variable=element_type)

    if element_id == 'undefined':
        start = True
        elements_selection = Sample.objects.filter(type=type_class)
        elements_id = list()
        for e in elements_selection:
            elements_id.append(e.id)
        elements_id.sort()
        element_id = elements_id[0]
    element = Sample.objects.get(pk=element_id)
    element_options = list()
    for option in element.options.split(';'):
        if option != '':
            element_options.append(option)
    random.shuffle(element_options)

    return render(request, 'histology/test.html', locals())


# Страница статистики
def histology_stat(request, element_type):
    type_class = SampleType.objects.get(variable=element_type)

    # Если пользователь зарегистрирован, то загрузить статистику
    if request.user.is_authenticated:
        user_info = UserInfo.objects.get(user=request.user)
        user_data = user_info.get_data()
        correct = user_data["histology" + "_" + element_type]['correct']
        incorrect = user_data["histology" + "_" + element_type]['incorrect']
        incorrect_list = list()
        for e in user_data["histology" + "_" + element_type]['incorrect_list']:
            incorrect_list.append(Sample.objects.get(pk=e))

        total = len(Sample.objects.filter(type=type_class))
        correct_percent = round((int(correct) / total) * 100)
        incorrect_percent = 100 - correct_percent

    return render(request, 'histology/stat.html', locals())
