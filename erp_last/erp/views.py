
from django.shortcuts import render
from .models import Incumbent
import pandas as pd

import os
import csv

import datetime
import xlwt

from django.http import HttpResponse

def home(request):
    user = request.user
    return render(request,'base.html',{'user':user})

def product(request) :
    return render(request,'product.html')

def coa(request) :
    return render(request,'COA.html')
    
def coaDetail(request,pk) :
    return render(request,'COA_detail.html')

def productDetail(request,pk) :
    return render(request,'product_detail.html')

def incumbent(request) :
    return render(request,'incumbent.html')

def incumbentDetail(request,pk) :
    return render(request,'incumbent_detail.html')

def incumbent_download(request) :

    db_data = Incumbent.objects.all().values()
    pd_db_data = pd.DataFrame(db_data)

    data = db_data
    response = HttpResponse(content_type="application/vnd.ms-excel")
    response["Content-Disposition"] = 'attachment; filename=HR_' + str(datetime.date.today()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('sheet01')
    title_style = xlwt.easyxf('pattern: pattern solid, fore_color indigo; align: horizontal center; font: color_index white;')
    data_style = xlwt.easyxf('align: horizontal right')

    col_names = pd_db_data.columns.values

    rows = []
    temp = []
    row_num = 0

    for datum in data:
        for i in col_names :
            temp.append(datum[i])
        rows.append(temp)
        temp = []

    for idx, col_name in enumerate(col_names):
        if col_name == "부서_id" : col_name = "부서"
        ws.write(row_num, idx, col_name, title_style)

    for row in rows:
        row_num +=1
        for col_num, attr in enumerate(row):
            if type(attr) == datetime.date : 
                attr = str(attr)
            ws.write(row_num, col_num, attr, data_style)

    wb.save(response)
    
    return response

def incumbent_upload(request) :
    return render(request,'incumbent_upload.html')

def retiree(request) :
    return render(request,'retiree.html')

def login(request) :
    return render(request,'login.html')

def register(request) :
    return render(request,'register.html')

