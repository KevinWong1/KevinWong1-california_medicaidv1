from django.shortcuts import render
# from get_new_data import *
# Create your views here.
from california_medicaid.get_new_data import *
from bs4 import BeautifulSoup
import requests


def index(request):

    req = requests.get(
        'https://raw.githubusercontent.com/KevinWong1/KevinWong1-california_medicaidv1/main/california_medicaid/website.html')
    soup = BeautifulSoup(req.content, 'html.parser')
    list_of_dictionary = []
    y = soup.select('.ffitem .body-sml span')
    for x in y:
        temp_dictionary = {}
        a = x.select('h3')
        for _ in a:
            temp_dictionary['drug_name'] = _.getText()
        b = x.select('p')

        for _ in b:
            if 'cd1' in str(_):
                temp_dictionary['restricted'] = _.getText()
            elif 'codes' in str(_):
                temp_dictionary['code'] = _.getText()
            else:
                temp_dictionary['other'] = _.getText()
        if temp_dictionary:
            list_of_dictionary.append(temp_dictionary)

    sorted_list = sorted(list_of_dictionary, key=lambda i: i['drug_name'])
    # print(sorted_list)

    context = {'medicaid': sorted_list}
    return render(request, 'california_medicaid/index.html', context)
