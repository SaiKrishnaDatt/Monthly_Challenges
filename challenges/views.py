from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.

def january(request):
    return HttpResponse("This works!")
def february(request):
    return HttpResponse("Below are the todo for february")

def monthly_challenges(request,month):
    responseText = None;
    if month == "january":
        responseText= "5K per day"
    elif month == "february" :
        responseText = "5K per day + 30mins yoga"
    elif month == "march" :
        responseText = "10K per day"
    else :
        return HttpResponseNotFound("The url is incorrect, month at the end of the url is not valid one");
    return HttpResponse(responseText)

