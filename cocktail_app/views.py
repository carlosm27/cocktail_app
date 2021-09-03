from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Cocktail
import requests
# Create your views here.

def cocktail(request):
    cocktails={}
    if 'name' in request.GET:
        name=request.GET['name']
        url='https://www.thecocktaildb.com/api/json/v1/1/search.php?s=' f'{name}'
        response=requests.get(url)
        data=response.json()
        drinks=data['drinks']

        for drink in drinks:
            drink_information=Cocktail(
                name=drink["strDrink"],
                category=drink["strCategory"],
                instructions=drink['strInstructions'],
                ingredients=drink['strIngredient1'],
                measures=drink['strMeasure1'],
                image_url=drink["strDrinkThumb"]
            )
            drink_information.save()
            cocktails=Cocktail.objects.all()
    context= {"cocktails": cocktails}
    return render(request,"cockatail_app/cocktails.html", context)



def cocktail_detail(request,id):
    drink_details=Cocktail.objects.get(id=id)
    context={'drink_details':drink_details}
    return render(request,'cockatail_app/cocktail_detail.html',context)

