from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    """注册新用户"""
    if request.method != 'post':
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单已提交
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，再重新定向到主页我重新有修改了进行commit提交
            login(request,new_user)
            return redirect('learning_ogs:index')
    content = {'form': form}
    return render(request,'registration/register.html',content)

