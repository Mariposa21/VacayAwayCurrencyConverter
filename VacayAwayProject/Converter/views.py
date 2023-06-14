from decimal import Decimal
from django.forms import Form
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .businessLogic import manageAlphaAdvantageAPICall
from .models import vacation as Vacation, costCategory as CostCategory


def home(request):
    if request.method == 'POST': 
        vacay_form = VacationForm(request.POST)
        costCategoryRequestList = request.POST.getlist('costCategory')
        cost_category_forms = []
        for index, value in enumerate(costCategoryRequestList):
            newCostCategoryForm = CostCategoryForm(request.POST)
            newCostCategoryForm.costCategory = value
            newCostCategoryForm.originCostAmount = request.POST.getlist('originCostAmount')[index]
            cost_category_forms.append(newCostCategoryForm)
        if vacay_form.is_valid(): 
            apiCallVacay = manageAlphaAdvantageAPICall(vacay_form) 
            request.POST._mutable = True
            savedVacay = vacay_form.save(commit=False)   
            savedVacay.latestConversionRate = apiCallVacay.latestConversionRate
            savedVacay.save()
            for costCategoryForm in cost_category_forms:
                newCostCategoryForm = costCategoryForm.save(commit=False)
                newCostCategoryForm.vacationId = savedVacay.vacationId
                newCostCategoryForm.vacation = savedVacay
                newCostCategoryForm.costCategory = costCategoryForm.costCategory
                newCostCategoryForm.originCostAmount = costCategoryForm.originCostAmount
                newCostCategoryForm.arrivalCostAmount = Decimal(savedVacay.latestConversionRate) * Decimal(costCategoryForm.originCostAmount)
                newCostCategoryForm.save()
            return redirect('converterResult', pk=savedVacay.vacationId)
        else: 
            return HttpResponse("Issues with vacay form.")
    else:
        vacay_form = VacationForm()
        categoryContext = {}
        for x in costCategory.COST_CATEGORIES: 
            cost_category_form = CostCategoryForm()
            cost_category_form.populateFormRow(x[0])
            categoryContext[x[0]+'_form'] = cost_category_form
        context = {
            'vacay_form': vacay_form, 
            'forms': categoryContext, 
            'costCategoryValues': CostCategory.COST_CATEGORIES
        }
        return render(request, 'Converter/home.html', context)
    
def converterResult(request, pk):
    vacationforEval = Vacation.objects.filter(vacationId=pk)[0]
    costCategoryList = CostCategory.objects.filter(vacation=vacationforEval)
    totalArrivalCostAmount = Decimal(0.00)

    costCategoryListContext = {}
    for costCategoryItem in costCategoryList: 
        costCategoryResult = {
            'costCategory' : costCategoryItem.costCategory, 
            'originCostAmount' : costCategoryItem.originCostAmount, 
            'arrivalCostAmount' : costCategoryItem.arrivalCostAmount
        }
        costCategoryListContext[costCategoryItem.costCategory+'_result'] = costCategoryResult
        totalArrivalCostAmount = costCategoryItem.arrivalCostAmount + totalArrivalCostAmount

    context = { 
        'vacationContext': vacationforEval, 
        'costCategoryList': costCategoryListContext, 
        'costCategoryValues': CostCategory.COST_CATEGORIES, 
        'totalArrivalCostAmount': totalArrivalCostAmount
    }
        
    return render(request, 'Converter/converterResult.html', context)
    