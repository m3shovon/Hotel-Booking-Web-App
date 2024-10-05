# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.decorators import login_required
# from .forms import SignupForm, LoginForm
# from .models import User

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('hotel_list')
#     else:
#         form = SignupForm()
#     return render(request, 'signup.html', {'form': form})

# def signin(request):
#     if request.method == 'POST':
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('username')  # Email in this case
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('hotel_list')
#     else:
#         form = LoginForm()
#     return render(request, 'signin.html', {'form': form})
