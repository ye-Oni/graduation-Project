from django.shortcuts import render
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False) #commit=False이기 때문에 db에 저장하지 않고 메모리 상에 객체만 만들어진 상태
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'registration/register_done.html',{'new_user':new_user})
    else:
            user_form = RegisterForm()
    return render(request,'registration/register.html',{'form':user_form})

def mainpage(request):
    return render(request,'registration/main.html')