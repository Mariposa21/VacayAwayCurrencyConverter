# VacayAwayCurrencyConverter :moneybag: :airplane:

## Project Summary: 
When I plan out a vacation in a destination that does not use American currency, I always find myself doing math in my head when reading different travel websites about the destination that talk about different activities, hotels, restaurants in the destination currency. For example, 120 Euros average for a hotel night stay in a great city versus 80 for the equivalent just outside the city translates to what colloquial dollar amount exactly? Sure, standard hotels websites do handle currency conversion. However, having a translation of the dollar amount is helpful, particularly when out-and-about in the travel destination and spending money on restaurant outings or activities.
As a potential solution, the VacayAwayCurrencyConverter was created via the Django framework, primarily coded in Python.

## Project Screenshare: 
<div align="center" style="display: flex; flex-direction: row;">
 <video class="video" src="https://github.com/Mariposa21/VacayAwayCurrencyConverter/assets/90941845/475d6c02-c62c-46de-bc01-77570c5d0875" />
</div>

## Project Tech Stack: 
1. Django Framework Python Project.
2. HTML pages use combination of HTML and JavaScript, with CSS styling.
3. SqlLite is used for data store. 
4. AlphaVantage API is used to get latest currency conversion rate for requested currency conversion.

## Future Enhancement Items: 
1. Add conversion fee as optional parameter in case user also wishes to budget for this. This is partially built-out already at the database level. 
2. Add database-level logging to application. 
