from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)
    
    
@csrf_exempt
def register_flutter(request):

    if request.method == 'POST':

        try:

            data = request.POST

            username = data.get('username')

            password = data.get('password')

            if not username or not password:

                return JsonResponse({'message': 'Username and password are required.'}, status=400)




            # Additional validation checks can be added here (e.g., password strength, existing user check)




            user = User.objects.create(username=username, password=make_password(password))

            return JsonResponse({'message': 'User registered successfully.'}, status=201)

        except Exception as e:

            return JsonResponse({'message': str(e)}, status=500)

    else:

        return JsonResponse({'message': 'Invalid request method.'}, status=405)