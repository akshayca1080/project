from django.shortcuts import render,redirect
from .forms import Form
from .models import Post

def post_list(request):
    if request.method=='POST':
        form=Form(request.POST or None,request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form=Form()
    context={
        'form':form
    }
    return render(request, 'upload/post_list.html', context)

def teacher_view(request):
    queryset=Post.objects.all()
    context={
        'object_list':queryset,
      
    }
    
    return render(request,'upload/view.html',context)
