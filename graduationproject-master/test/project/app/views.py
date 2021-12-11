from django.shortcuts import render
#from django.http import HttpResponse
#from Untitled import test
from .models import Test


import scipy as sp
import pandas as pd
import numpy as np
import csv
import surprise

import warnings
# Create your views here.

#def bar(request):


def index(request):
    test = Test.objects
    return render(request, 'index.html', {'tests':test})

def new(request):
    test = Test()
    test.name = request.POST.get('name')
    test.local = request.POST.get('local')
    test.rating = request.POST.get('rating')
    test.save()

    if(request.POST.get('q1')=='1'):
        if (request.POST.get('q2') == '1'):
            if (request.POST.get('q3') == '1'):
                f = open('static/뚜벅혼자관광.csv', 'a', newline='', encoding='utf-8')
                wr = csv.writer(f)
                wr.writerow([test.name, test.local, test.rating])
                f.close()

                warnings.filterwarnings('ignore')
                data = pd.read_csv('static/뚜벅혼자관광.csv', encoding="utf-8", sep=",")
            elif(request.POST.get('q3') == '2'):
                f = open('static/뚜벅혼자휴양.csv', 'a', newline='', encoding='utf-8')
                wr = csv.writer(f)
                wr.writerow([test.name, test.local, test.rating])
                f.close()

                warnings.filterwarnings('ignore')
                data = pd.read_csv('static/뚜벅혼자휴양.csv', encoding="utf-8", sep=",")
        elif (request.POST.get('q2') == '2'):
            if (request.POST.get('q3') == '1'):
                f = open('static/뚜벅2인관광.csv', 'a', newline='', encoding='utf-8')
                wr = csv.writer(f)
                wr.writerow([test.name, test.local, test.rating])
                f.close()

                warnings.filterwarnings('ignore')
                data = pd.read_csv('static/뚜벅2인관광.csv', encoding="utf-8", sep=",")

            elif (request.POST.get('q3') == '2'):
                f = open('static/뚜벅2인휴양.csv', 'a', newline='', encoding='utf-8')
                wr = csv.writer(f)
                wr.writerow([test.name, test.local, test.rating])
                f.close()

                warnings.filterwarnings('ignore')
                data = pd.read_csv('static/뚜벅2인휴양.csv', encoding="utf-8", sep=",")
        elif (request.POST.get('q2') == '3'):
            if (request.POST.get('q3') == '1'):
                f = open('static/뚜벅3인관광.csv', 'a', newline='', encoding='utf-8')
                wr = csv.writer(f)
                wr.writerow([test.name, test.local, test.rating])
                f.close()

                warnings.filterwarnings('ignore')
                data = pd.read_csv('static/뚜벅3인관광.csv', encoding="utf-8", sep=",")

            elif (request.POST.get('q3') == '2'):
                f = open('static/뚜벅3인휴양.csv', 'a', newline='', encoding='utf-8')
                wr = csv.writer(f)
                wr.writerow([test.name, test.local, test.rating])
                f.close()

                warnings.filterwarnings('ignore')
                data = pd.read_csv('static/뚜벅3인휴양.csv', encoding="utf-8", sep=",")

    elif(request.POST.get('q1')=='2'):
        if (request.POST.get('q2') == '1'):
            if (request.POST.get('q3') == '1'):
                f = open('static/자차혼자관광.csv', 'a', newline='', encoding='utf-8')
                wr = csv.writer(f)
                wr.writerow([test.name, test.local, test.rating])
                f.close()

                warnings.filterwarnings('ignore')
                data = pd.read_csv('static/자차혼자관광.csv', encoding="utf-8", sep=",")
            elif(request.POST.get('q3') == '2'):
                f = open('static/자차혼자휴양.csv', 'a', newline='', encoding='utf-8')
                wr = csv.writer(f)
                wr.writerow([test.name, test.local, test.rating])
                f.close()

                warnings.filterwarnings('ignore')
                data = pd.read_csv('static/자차혼자휴양.csv', encoding="utf-8", sep=",")
        elif (request.POST.get('q2') == '2'):
            if (request.POST.get('q3') == '1'):
                f = open('static/자차2인관광.csv', 'a', newline='', encoding='utf-8')
                wr = csv.writer(f)
                wr.writerow([test.name, test.local, test.rating])
                f.close()

                warnings.filterwarnings('ignore')
                data = pd.read_csv('static/자차2인관광.csv', encoding="utf-8", sep=",")

            elif (request.POST.get('q3') == '2'):
                f = open('static/자차2인휴양.csv', 'a', newline='', encoding='utf-8')
                wr = csv.writer(f)
                wr.writerow([test.name, test.local, test.rating])
                f.close()

                warnings.filterwarnings('ignore')
                data = pd.read_csv('static/자차2인휴양.csv', encoding="utf-8", sep=",")
        elif (request.POST.get('q2') == '2'):
            if (request.POST.get('q3') == '3'):
                f = open('static/자차3인관광.csv', 'a', newline='', encoding='utf-8')
                wr = csv.writer(f)
                wr.writerow([test.name, test.local, test.rating])
                f.close()

                warnings.filterwarnings('ignore')
                data = pd.read_csv('static/자차3인관광.csv', encoding="utf-8", sep=",")

            elif (request.POST.get('q3') == '2'):
                f = open('static/자차3인휴양.csv', 'a', newline='', encoding='utf-8')
                wr = csv.writer(f)
                wr.writerow([test.name, test.local, test.rating])
                f.close()

                warnings.filterwarnings('ignore')
                data = pd.read_csv('static/자차3인휴양.csv', encoding="utf-8", sep=",")


    

    df = data[['id', '여행지', 'rating']]

    def recur_dictify(frame):
        if len(frame.columns) == 1:
            if frame.values.size == 1: return frame.values[0][0]
            return frame.values.squeeze()
        grouped = frame.groupby(frame.columns[0])
        d = {k: recur_dictify(g.iloc[:, 1:]) for k, g in grouped}
        return d

    df_to_dict = recur_dictify(df)

    name_list = []
    cos_set = set()

    for user_key in df_to_dict:
        name_list.append(user_key)
        for cos_key in df_to_dict[user_key]:
            cos_set.add(cos_key)

    local_list = list(cos_set)

    rating_dic = {
        'id': [],
        '여행지': [],
        'rating': []
    }

    for name_key in df_to_dict:
        for cos_key in df_to_dict[name_key]:
            a1 = name_list.index(name_key)
            a2 = local_list.index(cos_key)
            a3 = df_to_dict[name_key][cos_key]

            rating_dic['id'].append(a1)
            rating_dic['여행지'].append(a2)
            rating_dic['rating'].append(a3)

    df = pd.DataFrame(rating_dic)

    reader = surprise.Reader(rating_scale=(1, 10))
    data = surprise.Dataset.load_from_df(df[['id', '여행지', 'rating']], reader)

    trainset = data.build_full_trainset()
    option = {'name': 'pearson'}
    algo = surprise.KNNBasic(sim_options=option)

    algo.fit(trainset)

    index = name_list.index(test.name)
    result = algo.get_neighbors(index, k=2)

    def localtest():
        for r1 in result:
            max_rating=data.df[data.df["id"]==r1]["rating"].max()
            local_id=data.df[(data.df["rating"]==max_rating)&(data.df["id"]==r1)]["여행지"].values
            for local_item in local_id:
                return(local_list[local_item])
    return render(request, 'result.html',{'localtest':localtest})
