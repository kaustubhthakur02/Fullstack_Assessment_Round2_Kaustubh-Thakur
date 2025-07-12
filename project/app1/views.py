
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .models import User

def login_page(request):
    return render(request, 'login.html')

@csrf_exempt
@require_http_methods(["POST"])
def authenticate_user(request):
    try:
        data = json.loads(request.body)
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({"status": "fail"})
        except User.DoesNotExist:
            return JsonResponse({"status": "fail"})
            
    except json.JSONDecodeError:
        return JsonResponse({"status": "fail"})
    except Exception as e:
        return JsonResponse({"status": "fail"})