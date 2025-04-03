from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    if request.user.user_type == "donor":
        return render(request, "dashboard/donor_home.html")
    elif request.user.user_type == "receiver":
        return render(request, "dashboard/receiver_home.html")
    else:
        return redirect('login_view')

# def donor_home_view(request):
#     return render(request, "dashboard/donor_home.html", {"user": request.user})

# def receiver_home_view(request):
#     return render(request, "dashboard/receiver_home.html", {"user": request.user})
