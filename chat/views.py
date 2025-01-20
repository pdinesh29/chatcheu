from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
def login(request):
    if 'id' in request.session:
        return redirect(reverse("home"))
    else:
        return render(request,"login.html")
def home(request):
    if request.method=='GET':
        if "id" not in request.session:
            request.session["wrongp"]=False
            return redirect('login')
        else:
            print(request.session['id'])
            return render(request, "home.html", {
                    # "nums": Alloted.objects.filter(faculty=request.session['id']),
                })
    if request.method == 'POST':
        # email = request.POST.get('phoneno')
        # password = request.POST.get('pass')
        # try:
        #     faculty = Faculty.objects.get(email=email,password=password)
        #     request.session['id']=faculty.id
        #     return render(request, "home.html", {
        #             "nums": Alloted.objects.filter(faculty=faculty),
        #         })
        # except Faculty.DoesNotExist:
        #     request.session['wrongp']=True
        #     return redirect('login')
        return render(request,'home.html')
    return redirect('login')
def logout(request):
    request.session.flush()
    return redirect('home')