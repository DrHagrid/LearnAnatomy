from django.http import JsonResponse
from django.shortcuts import render
from content.models import Bone, BoneType
from content.models import element_types, element_groups
from users.models import UserInfo
import random


def check_answer(request):
    return_dict = dict()
    data = request.POST
    answer = data.get("answer")
    element_group = data.get("element_group")
    element_type = data.get("element_type")
    element_id = data.get("element_id")
    element = element_groups.get(element_group).objects.get(pk=element_id)

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

    #element_number = len(element.objects.all())
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

        #user_info = UserInfo.objects.get(user=request.user)
        #user_info.last_reaction = next_bone_id
        #user_info.save(force_update=True)

        return_dict["response"] = True
        return_dict["element_group"] = element_group
        return_dict["element_type"] = element_type
        return_dict["next_element_id"] = next_element_id
        return_dict["name_lat"] = element.name_lat
        return_dict["info"] = element.info

    return JsonResponse(return_dict)
