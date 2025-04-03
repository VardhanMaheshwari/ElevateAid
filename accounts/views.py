from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
import json

def register_page(request):
    return render(request, 'accounts/register.html')

def login_page(request):
    return render(request, 'accounts/login.html')

@csrf_exempt
def api_user_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        logo = request.FILES.get("logo")

        user_type = data.get("user_type")
        sub_type = data.get("sub_type")
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        address = data.get("address")
        password = data.get("password")
        print(password)
        print(email)
        if not all([name, email, phone, address, password]):
            return JsonResponse({"success": False, "message": "All fields are required!"}, status=400)
        
        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "message": "Email is already registered!"}, status=400)
        
        if CustomUser.objects.filter(phone=phone).exists():
            return JsonResponse({"success": False, "message": "Phone number is already registered!"}, status=400)
        
        if sub_type in ["ngo", "college", "company"]:
            ngo_college_company_id = data.get("ngo_college_company_id")
            if not ngo_college_company_id:
                return JsonResponse({"success": False, "message": "ID is required for NGOs, Colleges, and Companies."}, status=400)
            if CustomUser.objects.filter(ngo_college_company_id=ngo_college_company_id).exists():
                return JsonResponse({"success": False, "message": "This ID is already registered!"}, status=400)
        
        elif sub_type == "personal":
            aadhar_number = data.get("aadhar_number")
            if not aadhar_number:
                return JsonResponse({"success": False, "message": "Aadhar number is required for personal users."}, status=400)
            if CustomUser.objects.filter(aadhar_number=aadhar_number).exists():
                return JsonResponse({"success": False, "message": "Aadhar number is already registered!"}, status=400)
        
        user = CustomUser.objects.create(
            name=name,
            email=email,
            password=make_password(password),
            phone=phone,
            address=address,
            user_type=user_type,
            sub_type=sub_type,
            ngo_college_company_id=data.get("ngo_college_company_id", ""),
            aadhar_number=data.get("aadhar_number", ""),
            logo=logo,
        )
        return JsonResponse({"success": True, "message": "User registered successfully!"}, status=201)

@csrf_exempt
def api_user_login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(request, username=email, password=password)
        
        if user:
            login(request, user)
            request.session['user_type'] = user.user_type
            # return redirect('api_home')
            return JsonResponse({"success": True, "message": "Login successful!"}, status=200)
        else:
            return JsonResponse({"success": False, "message": "Invalid email or password!"}, status=401)
    
    return JsonResponse({"success": False, "message": "Invalid request method!"}, status=400)

@csrf_exempt
def api_user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login_view')
    else:
        return redirect('login_view')
