from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from table.models import vacancies

# Create your views here.

def main_vacancies(request):
    temp_data = vacancies.objects.values()
    data = []
    for objectt in temp_data:
        data.append({"id" : objectt["id_of_vacancie"],
                    "name" : objectt["name"], 
                    "description" : objectt['description'], 
                    "status" : objectt['status'], 
                    "rubr_atrub" : objectt['rubr_atrub'], 
                    "conter_name" : objectt['conter_name'], 
                    "file_or_link" : objectt['file_or_link'], 
                    "prefix" : objectt['prefix'],
                    "source" : objectt['source'],
                    "date" : objectt["date"]})

    return render(request, template_name="tablale.html", context={"data" : data})

def edit_for_id(request):
    if request.method == "GET":
        if request.GET.get("id") \
        and request.GET.get("name") \
        and request.GET.get("description") \
        and request.GET.get("status") \
        and request.GET.get("rubr_atrub") \
        and request.GET.get("conter_name") \
        and request.GET.get("file_or_link") \
        and request.GET.get("prefix"):
            data = {
                    "id" : request.GET.get("id"),
                    "name" : request.GET.get("name"),
                    "description" : request.GET.get("description"),
                    "status" : request.GET.get("status"),
                    "rubr_atrub" : request.GET.get("rubr_atrub"),
                    "conter_name" : request.GET.get("conter_name"),
                    "file_or_link" : request.GET.get("file_or_link"),
                    "prefix" : request.GET.get("prefix")
                    }
            
            result = vacancies.objects.filter(id_of_vacancie = data['id'])

            result.update(name = data['name'],
                          description = data['description'],
                          status = data['status'],
                          rubr_atrub = data['rubr_atrub'],
                          conter_name = data['conter_name'],
                          file_or_link = data['file_or_link'],
                          prefix = data['prefix'])

            result = vacancies.objects.filter(id_of_vacancie = data['id']).values()

            return JsonResponse({"status" : True, "data" : result[0]})
        else: return JsonResponse({"status" : False, "text" : "Произошла ошибка, перезагрузите страницу и попробуйте ещё раз"})
    else: return JsonResponse({"status" : False, "text" : "this is a GET request"})

def new_edit_for_id(request):
    if request.method == "GET":
        if request.GET.get("id") \
        and request.GET.get("name") \
        and request.GET.get("date") \
        and request.GET.get("source"):
            data = {
                    "id" : request.GET.get("id"),
                    "name" : request.GET.get("name"),
                    "date" : request.GET.get("date"),
                    "source" : request.GET.get("source")
                    }
            result = vacancies.objects.filter(id_of_vacancie = data['id'])
            result.update(name = data['name'],
                          date = data['date'],
                          source = data['source'])

            result = vacancies.objects.filter(id_of_vacancie = data['id']).values()

            return JsonResponse({"status" : True, "data" : result[0]})
        else: return JsonResponse({"status" : False, "text" : "Произошла ошибка, перезагрузите страницу и попробуйте ещё раз"})
    else: return JsonResponse({"status" : False, "text" : "this is a GET request"})



def add_vacancies(request):
    if request.method == "GET":
        if request.GET.get("id") \
        and request.GET.get("name") \
        and request.GET.get("description") \
        and request.GET.get("status") \
        and request.GET.get("rubr_atrub") \
        and request.GET.get("conter_name") \
        and request.GET.get("file_or_link") \
        and request.GET.get("prefix"):
            data = {
                    "id" : request.GET.get("id"),
                    "name" : request.GET.get("name"),
                    "description" : request.GET.get("description"),
                    "status" : request.GET.get("status"),
                    "rubr_atrub" : request.GET.get("rubr_atrub"),
                    "conter_name" : request.GET.get("conter_name"),
                    "file_or_link" : request.GET.get("file_or_link"),
                    "prefix" : request.GET.get("prefix")
                    }
            if not len(vacancies.objects.filter(id_of_vacancie = data["id"])) >= 1:
                vacancies.objects.create(
                            id_of_vacancie = str(data['id']),
                            name = data['name'],
                            description = data['description'],
                            status = data['status'],
                            rubr_atrub = data['rubr_atrub'],
                            conter_name = data['conter_name'],
                            file_or_link = data['file_or_link'],
                            prefix = data['prefix'])
                return JsonResponse({"status" : True})
            else: return JsonResponse({"status" : False, "text" : "Такой айди вакансии уже существует"})
        else: return JsonResponse({"status" : False, "text" : "Произошла ошибка, перезагрузите страницу и попробуйте ещё раз"})
    else: return JsonResponse({"status" : False, "text" : "this is a GET request"})

def delete_vacancies(request):
    if request.method == "GET":
        if request.GET.get("id"):
            data = {
                    "id" : request.GET.get("id")
                    }
            
            if len(vacancies.objects.filter(id_of_vacancie = data["id"])) >= 1:
                vacancies.objects.filter(id_of_vacancie = data['id']).delete()
                return JsonResponse({"status" : True})
            else: return JsonResponse({"status" : False, "text" : "Такого айди больше не существует"})
            
        else: return JsonResponse({"status" : False, "text" : "Произошла ошибка, перезагрузите страницу и попробуйте ещё раз"})
    else: return JsonResponse({"status" : False, "text" : "this is a GET request"})

def main_search(request):
    temp_data = vacancies.objects.values()
    data = []
    for objectt in temp_data:
        data.append({"id_of_vacancie" : objectt["id_of_vacancie"],
                    "name" : objectt["name"], 
                    "description" : objectt['description'], 
                    "status" : objectt['status'], 
                    "rubr_atrub" : objectt['rubr_atrub'], 
                    "conter_name" : objectt['conter_name'], 
                    "file_or_link" : objectt['file_or_link'], 
                    "prefix" : objectt['prefix']})

    return render(request, template_name="search.html", context={"data" : data})

def all_data(request):
    temp_data = vacancies.objects.values()
    data = []
    for objectt in temp_data:
        data.append({"id" : objectt["id_of_vacancie"],
                    "name" : objectt["name"], 
                    "description" : objectt['description'], 
                    "status" : objectt['status'], 
                    "rubr_atrub" : objectt['rubr_atrub'], 
                    "conter_name" : objectt['conter_name'], 
                    "file_or_link" : objectt['file_or_link'], 
                    "prefix" : objectt['prefix'],
                    "source" : objectt['source'],
                    "date" : objectt["date"]})
    return JsonResponse({"status" : True, "data" : data})


def card(request):
    if request.GET.get("id"):
        temp_data = vacancies.objects.values().filter(id_of_vacancie=request.GET.get("id"))
        data = None
        for objectt in temp_data:
            data = {
                        "id" : objectt["id_of_vacancie"],
                        "name" : objectt["name"], 
                        "description" : objectt['description'], 
                        "status" : objectt['status'], 
                        "rubr_atrub" : objectt['rubr_atrub'], 
                        "conter_name" : objectt['conter_name'], 
                        "file_or_link" : objectt['file_or_link'], 
                        "prefix" : objectt['prefix'],
                        "source" : objectt['source'],
                        "date" : objectt["date"],
                        "category" : objectt["category"],
                        "contacts" : objectt["contacts"], 
                        "zp" : objectt["zp"]}
        
        print(type(data))

        return render(request, "card.html", data)
    
def test(request):
    temp_data = vacancies.objects.values().filter(id_of_vacancie=5)

    temp_data.update(category="Ненависть к деду")


    return HttpResponse("DA ")