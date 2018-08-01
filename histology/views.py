# -*- coding: utf-8 -*-
from django.http import JsonResponse
from django.shortcuts import render
from histology.models import Sample
from users.models import UserInfo
import random


# Проверка ответа
def histology_check(request):
    return_dict = dict()
    data = request.POST
    answer = data.get("answer")
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
        'Ответ не верный. Нажмите "Подсказка", если хотите посмотреть ответ.',
        'Не верно!'
    ])

    return_dict["replica_success"] = replica_success
    return_dict["replica_fail"] = replica_fail

    if answer == "correct":  # При условии верного ответа
        elements_selection = Sample.objects.all()
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

        return_dict["next_element_id"] = next_element_id
        return_dict["correct_option"] = element.correct_option
        return_dict["info"] = element.info
    else:
        response = 'False'

    # Если пользователь зарегистрирован, то сохранить статистику
    # if request.user.is_authenticated:
    #     user_info = UserInfo.objects.get(user=request.user)
    #
    #     if user_info.data:
    #         user_data = user_info.get_data()
    #     else:
    #         user_data = dict()
    #
    #     if response == 'True':
    #         if start == 'True':
    #             user_data[element_group + "_" + element_type] = {'correct': 0, 'incorrect': 0, 'incorrect_list': []}
    #         user_data[element_group + "_" + element_type]['correct'] += 1
    #     else:
    #         if start == 'True':
    #             user_data[element_group + "_" + element_type] = {'correct': 0, 'incorrect': 0, 'incorrect_list': []}
    #         user_data[element_group + "_" + element_type]['incorrect'] += 1
    #         if not any(element_id in el for el in user_data[element_group + "_" + element_type]['incorrect_list']):
    #             user_data[element_group + "_" + element_type]['incorrect_list'].append(element_id)
    #     user_info.set_data(user_data)
    #     user_info.save(force_update=True)

    return_dict["response"] = response

    return JsonResponse(return_dict)


# Страница теста
def histology(request, element_id):
    if element_id == 'undefined':
        start = True
        elements_selection = Sample.objects.all()
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
def histology_stat(request, element_group, element_type):
    group_class = element_groups.get(element_group)
    type_class = element_types.get(element_group).objects.get(variable=element_type)

    # Если пользователь зарегистрирован, то загрузить статистику
    if request.user.is_authenticated:
        user_info = UserInfo.objects.get(user=request.user)
        user_data = user_info.get_data()
        correct = user_data[element_group + "_" + element_type]['correct']
        incorrect = user_data[element_group + "_" + element_type]['incorrect']
        incorrect_list = list()
        for e in user_data[element_group + "_" + element_type]['incorrect_list']:
            incorrect_list.append(group_class.objects.get(pk=e))

        total = len(group_class.objects.filter(type=type_class))

    return render(request, 'histology/stat.html', locals())
