from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.


def pc_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            
            if user.club_name == 'PROGRAMMING' and user.user_type != 'MEMBERS':
                    messages.success(request, 'Successfully logged in')
                    return redirect('dashboard')
            # elif user.club_name == 'DEVELOPMENT':
            #     messages.warning(request, 'Invalid User Tyep')
            #     return redirect('pc_login')
            elif user.club_name == 'DEVELOPMENT' and user.user_type != 'MEMBERS':
                    messages.success(request, 'Successfully logged in')
                    return redirect('dev_dashboard')
            else:
                messages.success(request, 'Successfully logged in')
                return redirect('home')
        else:
            messages.warning(request, 'Invalid User')
            return redirect('pc_login')
    return render(request,'user_account/login.html')


def pc_logout(request):
    logout(request)
    return redirect('pc_login')
