from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# Create your views here.
def home_view(request,*args,**kwargs):
    context={ 
        "resto":[['mcd','mulund','fries'],['subway','vashi','salads']]

   }
    context["resto"][0].append(12.0)
    context["resto"][1].append('1')
    context["resto"].append(['joey'])
    # my_context ={
    #     "1":1
        
    # }
    # asd = {
    #     "context": context,
    #     "my_context": my_context 
    # }

    
    
    return render(request,"index.html",context)

def contact_view(request,*args,**kwargs):
    # return HttpResponse("<h1>contact the idiot</h1>")
    my_context ={
        "my_text": "this is contact",
        "my_number": 12345,
        "my_list" : [2,'blah',3.90,'ll'],
        "htmlyo": "<i class='fas fa-h1'>hello world</i>",
    }
    
    return render(request,"contact.html",my_context)


def feedback_view(request,*args,**kwargs):
    variable= {
        "price" : [x for x in range(pow(10,3)) ]

    }
    print(variable["price"])
    return render(request,"feedback.html",variable)



def blog_view(request,*args,**kwargs):
    objec = Blog.objects.get(id)
    context = {"object"  : objec} 
    template_naam = "feedback.html"
    template_ka_obj = get_template(template_naam)
    return HttpResponse(template_ka_obj.render(context))


