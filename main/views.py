from django.shortcuts import render,redirect
from .models import Delhi,Contact
from django.contrib import messages
from django.template import loader


# Create your views here.
def index(request):
    return render(request ,'index.html')

def explore_delhi(request):
    explore_delhi= Delhi.objects.all()
    return render(request,'delhi.html',{'explore_delhi':explore_delhi})
def contact_us(request):
    if request.method == "POST":
            name =request.POST['name']
            email =request.POST['email']
            subject =request.POST['subject']
            message =request.POST['message']
            contact =Contact.objects.create(name=name,email=email,subject=subject,message=message)
            contact.save()
            messages.info(request,"Thanks for Submitting")
    
    return redirect('/')
def prims(request):
    
    INF = 9999999
# number of vertices in graph
    N = 4
#creating graph by adjacency matrix method
    G = [[0, 21.8, 7, 8.1, 9.1,15,7.7],
         [21.8, 0, 12.2, 18.7, 11.4,9.4,11.3],
         [7, 12.2, 0, 9.8, 3.5,10.2,3.7],
         [7.2,18.7 ,6.9 , 0,10.1,16.1,8.8],
         [7.9,11.6 ,2.9 ,10.1 ,0,11.9,5.7],
         [14,10.4,11,11.3,12.5,0,5.8],
         [9.3,12.6,3,9,5.5,7.7,0],
         ]

    selected_node = [0, 0, 0, 0, 0,0,0]

    no_edge = 0

    selected_node[0] = True

# printing for edge and weight
    list_img = []
    list_img.append(str(Delhi.objects.get(pk=int(0)).img))
    while (no_edge < N-1):
    
        minimum = INF
        a = 0
        b = 0
        for m in range(N):
            if selected_node[m]:
                for n in range(N):
                    if ((not selected_node[n]) and G[m][n]):  
                    # not in selected and there is an edge
                        if minimum > G[m][n]:
                            minimum = G[m][n]
                            a = m
                            b = n
        
        
        selected_node[b] = True
        no_edge += 1
        prim =str(b)      
        for idx in prim:

            # list_img.append(Delhi.objects.get(pk=int(idx)).img)
            list_img.append(str(Delhi.objects.get(pk=int(idx)).img))
    print(list_img)
    messages.info(request,prim)       
    return render(request,'plan.html',{'prim':list_img})

    

