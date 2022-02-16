from django.shortcuts import render, redirect
from .forms import UploadFieldsForm
from .models import FieldsFiles, UploadFields
from django.db.models import Sum


def report_file_all(request):
    """ Function that returns all documents. """

    reports = FieldsFiles.objects.all()
    revenue = FieldsFiles.objects.aggregate(Sum('price'))
    revenue = revenue.get('price__sum')

    context = {
        'revenue': revenue,
        'reports': reports,
    }

    return render(request, 'report_all.html', context)


def report_file(request, pk):
    """ Function that returns the imported document. """

    files = UploadFields.objects.filter(id=pk)
    reports = FieldsFiles.objects.filter(upload_fields=pk)
    revenue = FieldsFiles.objects.filter(
        upload_fields=pk).aggregate(Sum('price'))
    revenue = revenue.get('price__sum')

    context = {
        'revenue': revenue,
        'reports': reports,
        'files': files,
    }

    return render(request, 'report_filter.html', context)


def upload_file(request):
    """ Function to import and index in the database. """

    upload_fields_form = UploadFieldsForm(
        request.POST or None, request.FILES or None)

    if request.method == "POST":
        if upload_fields_form.is_valid():
            response = process_file(request.FILES['file'])
            upload_fields_form.save()

            title = request.POST['title']
            id_title = UploadFields.objects.get(title=title).id
            response = create_volume(response, id_title)
            FieldsFiles.objects.bulk_create(
                FieldsFiles(**value) for value in response)

            return redirect('report/' + f'{id_title}')

    context = {
        'upload_fields_form': upload_fields_form,
    }

    return render(request, 'upload.html', context)


def process_file(file):
    """ Function to clear the return. """

    response = []
    for line in file:
        line = str(line, "utf-8")
        line = line.replace("\n", "")
        response.append(list(line.split("\t")))
    response.remove(response[0])

    return response


def create_volume(values, title):
    """ Function to create volume that will be indexed. """

    response = []
    for value in values:
        dict_insert = {}
        dict_insert.update({'upload_fields_id': title})
        dict_insert.update({"buyer": value[0]})
        dict_insert.update({"description": value[1]})
        dict_insert.update({"price": value[2]})
        dict_insert.update({"amounts": value[3]})
        dict_insert.update({"address": value[4]})
        dict_insert.update({"supplier": value[5]})
        response.append(dict_insert)

    return response
