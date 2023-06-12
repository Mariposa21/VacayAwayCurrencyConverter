from django.db import models

class vacation(models.Model): 
    vacationId = models.AutoField(primary_key=True)
    CURRENCY_OPTIONS = [("USD", "United States"), ("EUR","Italy"), 
                        ("EUR","Spain"), ("MXN","Mexico"), 
                        ("CAN","Canada")]
    countryOrigin = models.CharField(max_length=3, choices=CURRENCY_OPTIONS, default="USD", null=False)
    countryArrival = models.CharField(max_length=3, choices=CURRENCY_OPTIONS, default="MXN", null=False)
    conversionFee = models.DecimalField(max_digits=3, decimal_places=2, null=False, default=0.00)
    latestConversionRate = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

class costCategory(models.Model): 
    costCategoryId = models.AutoField(primary_key=True)
    COST_CATEGORIES = [("F", "Flight"), ("C", "Car/Vehicle Transportation"), ("O", "Food"), ("L", "Lodging"), ("M", "Miscellaneous/Extras"), ("A", "Activities")]
    costCategory = models.CharField(max_length=1, choices=COST_CATEGORIES, default="M")
    originCostAmount = models.DecimalField(max_digits=15, decimal_places=2, default=100.00)
    arrivalCostAmount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vacation = models.ForeignKey(vacation, on_delete=models.CASCADE, null=True, blank=True, db_column="vacationId") 

class conversionRateCurrency(models.Model): 
    conversionRateCurrencyId = models.AutoField(primary_key=True)
    CURRENCY_OPTIONS = [("USD", "United States"), ("EUR","Italy"), 
                        ("EUR","Spain"), ("MXN","Mexico"), 
                        ("CAN","Canada")]
    asOfDate = models.DateField(null=False)
    countryOrigin = models.CharField(max_length=3, choices=CURRENCY_OPTIONS, null=False)
    countryArrival = models.CharField(max_length=3, choices=CURRENCY_OPTIONS, null=False)
    exchangeRate = models.DecimalField(max_digits=15, decimal_places=2, choices=CURRENCY_OPTIONS, null=False, default=1.00)
    
    


