from django.shortcuts import render, redirect
from .forms import UploadFieldsForm
from .models import FieldsFiles


def report_file(request):
    reports = FieldsFiles.objects.all()

    context = {
        'reports': reports,
        'version': "version 0.0"
    }

    return render(request, 'home.html', context)


def upload_file(request):
    upload_fields_form = UploadFieldsForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if upload_fields_form.is_valid():
            response = process_file(request.FILES['file'])
            response = create_volume(response)
            FieldsFiles.objects.bulk_create(FieldsFiles(**user) for user in response)
            upload_fields_form.save()

            return redirect('upload_file:reports')

    context = {
        'upload_fields_form': upload_fields_form,
    }

    return render(request, 'upload.html', context)


def process_file(file):
    response = []
    for line in file:
        line = str(line, "utf-8")
        line = line.replace("\n", "")
        response.append(list(line.split("\t")))
    response.remove(response[0])

    return response


def create_volume(values):
    response = []
    for value in values:
        dict_insert = {}
        dict_insert.update({"buyer": value[0]})
        dict_insert.update({"description": value[1]})
        dict_insert.update({"price": value[2]})
        dict_insert.update({"amounts": value[3]})
        dict_insert.update({"address": value[4]})
        dict_insert.update({"supplier": value[5]})
        response.append(dict_insert)

    return response
