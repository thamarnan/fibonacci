from django.http import HttpResponse
import json
import datetime


def finalDisplay(finaltxt,n):
    data =  {
                "fibonanci" : [
                    {
                    'n': n,
                    'result': finaltxt,
                    }
                ]
            }
    return HttpResponse(json.dumps(data), content_type='application/json')

def fibonacci(request):
    number    = request.GET.get('n','')

    #Example http://ip.address/?n=5

    try:

        if '' in [number]:
            return finalDisplay("Invalid argument. Please provide valid n",-1)
        
        if number <= 0:
            return finalDisplay("Invalid argument. n cannot be less than 0",-1)
        
        if number == 1:
            return finalDisplay(list(0),number)
           
        count = 0
        n1 = 0
        n2 = 1 
        mylist = []
        mylist.append(n1)
        mylist.append(n2)
        
        if number >= 2:
           while count < number:
               mylist.append(n1)
               nextn = n1 + n2
               n1 = n2
               n2 = nextn
               count += 1
        
        return finalDisplay(mylist,number)
    execpt:
        return finalDisplay("Invalid n")