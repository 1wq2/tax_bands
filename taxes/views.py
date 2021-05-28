from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import TemplateView
from django.urls import reverse
from django.views.generic.edit import CreateView
import urllib.request
import sqlite3
from .forms import UploadFileForm, UrlForm, DataForm
from .models import Tax


class TaxView(APIView):
    def post(self, request):
        salary = self.request.data.get('salary')
        detailed = self.request.data.get('detailed') is not None
        if salary is None:
            raise Exception('Salary is not provided')
        try:
            salary = float(salary)
        except ValueError:
            raise Exception('Salary is not a number')
        if detailed:
            details = {}
            total = 0
            for tax in Tax.objects.all():
                curr_tax_value = tax.calculate_tax(salary)
                total += curr_tax_value
                details[f'{tax.begin} -> {tax.end or "inf"}'] = curr_tax_value
            return Response({'total_tax': total, 'details': details})
        else:

            return Response({'total_tax': Tax.calculate_total_tax(salary)})

def upload_file(request):
    res = 0
    details = ""
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            res = handle_uploading_file(request.FILES['file'])
            print(f'res --------> {res}')
    else:
        form = UploadFileForm()
    return render(request, 'taxes/upload_form.html', {'form': form, 'res': res, 'details': details})


def handle_uploading_file(f):
    text = f.read().decode().strip().replace(',', '')[1:]
    value = float(text)
    print(f'value--> {value}')

    total = calculate_tax(value)
    return total


def calculate_tax(income):
    tax = 0
    # tax20 = 7500  # (50000 - 12500) * 0.2
    # tax40 = 40000  # (150000 - 50000) * 0.4
    #
    #
    # if income < 12501:
    #     tax = 0
    # elif 12501 <= income < 50001:
    #     tax = (income - 12500) * 0.2
    # elif 50001 <= income < 150001:
    #     tax = (income - 50000) * 0.4 + tax20
    # elif income >= 150001:
    #     tax = (income - 150000) * 0.45 + tax40 + tax20
    return tax


def get_url_data(request):
    res = 0
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            res = handle_url_data(form.cleaned_data['url'])
    else:
        form = UrlForm()
    return render(request, 'taxes/url_form.html', {'form': form, 'res': res})


def handle_url_data(url):
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
        print(text)
        text = "£52,000"
        text = text.strip().replace(',', '')[1:]
        value = float(text)
        print(f'value--> {value}')

        total = calculate_tax(value)
        return total


def get_cloud_data(request):
    res = 0
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            res = handle_cloud_data(form.cleaned_data['url'])
    else:
        form = UrlForm()
    return render(request, 'taxes/cloud_form.html', {'form': form, 'res': res})


def handle_cloud_data(url):
    with urllib.request.urlopen(url) as f:
        text = f.read().decode('utf-8')
        print(text)
        text = "£52,000"
        text = text.strip().replace(',', '')[1:]
        value = float(text)
        print(f'value--> {value}')

        total = calculate_tax(value)
        return total


def get_db_data(request):
    data = []
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data = retrieve_db_data(request.FILES['file'].name)
            # handle_db_data(data)
    else:
        form = UploadFileForm()
    return render(request, 'taxes/db_form.html', {'form': form, 'data': data})


def retrieve_db_data(db):
    with sqlite3.connect(db) as db:
        cursor = db.cursor()
        sql = "select * from taxes"
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        print(data)
        return data


def handle_db_data(request):
    res = 0
    if request.method == 'POST':
        value = float(request.POST['salary'])
        print(f'value--> {value}')
        total = calculate_tax(value)
        res = total
    return render(request, 'taxes/db_form.html', {'res': res})
