from .models import *
import datetime
from alpha_vantage.foreignexchange import ForeignExchange
from dateutil.relativedelta import relativedelta

def manageAlphaAdvantageAPICall(vacationForm): 
    currentTimestamp = datetime.datetime.now()
    currentTimestampDate = currentTimestamp.date()
    vacationVariable = vacation()
    vacationVariable.originCurrency = vacationForm.cleaned_data['countryOrigin']
    vacationVariable.arrivalCurrency = vacationForm.cleaned_data['countryArrival']
    ##vacationVariable.conversionFee = vacationForm.cleaned_data['conversionFee']
    originCurrency = vacationVariable.countryOrigin
    arrivalCurrency = vacationVariable.countryArrival

    try:
        conversionRateCurrencyObj = conversionRateCurrency.objects.get(asOfDate=currentTimestampDate, countryOrigin=originCurrency, countryArrival=arrivalCurrency)
        vacationVariable.latestConversionRate = conversionRateCurrencyObj.exchangeRate
        return vacationVariable
    except (conversionRateCurrency.DoesNotExist):
        callAlphaAdvantageAPI(vacationVariable, currentTimestampDate)
        return vacationVariable

def callAlphaAdvantageAPI(vacation, currentTimestampDate): 
    apiKey = ''
    AV_Calls = ForeignExchange(key=apiKey)
    originCurrency = vacation.countryOrigin 
    arrivalCurrency = vacation.countryArrival

    #this is the actual AlphaVantage API call 
    exchangeData, metadata = AV_Calls.get_currency_exchange_monthly(originCurrency, arrivalCurrency, outputsize='compact')
    for key, value in sorted(exchangeData.items()):
        date = datetime.datetime.strptime(key, '%Y-%m-%d')
        dateTrimmed = date.date()
        dateDifference = abs(relativedelta(dateTrimmed, currentTimestampDate).days)
        if dateDifference <= 1:
            vacation.latestConversionRate = float((value['4. close'])) 
            break
    conversionRateCurrencyObj = conversionRateCurrency()
    conversionRateCurrencyObj.asOfDate = currentTimestampDate
    conversionRateCurrencyObj.exchangeRate = vacation.latestConversionRate
    conversionRateCurrencyObj.countryOrigin = originCurrency
    conversionRateCurrencyObj.countryArrival = arrivalCurrency
    conversionRateCurrencyObj.save()

    return vacation
            
