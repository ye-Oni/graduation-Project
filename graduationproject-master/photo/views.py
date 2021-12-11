from django.shortcuts import render,redirect
from .models import Photo
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.decorators import login_required #함수형 뷰에 사용
from django.contrib.auth.mixins import LoginRequiredMixin #클래스형 뷰에 사용
from django.contrib.auth.models import User
from django.core.paginator import Paginator


@login_required
def photo_list(request):
    photos = Photo.objects.all()
    return render(request,'photo/list.html',{'photos':photos})

class PhotoUploadView(LoginRequiredMixin,CreateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/upload.html'
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/photo')
        else:
            return self.render_to_response({'form':form})

# class PhotoDeleteView(LoginRequiredMixin,DeleteView):
#     model = Photo
#     success_url = '/'
#     template_name = 'photo/delete.html'

def photo_delete(request,pk):
    post = Photo.objects.get(pk=pk)
    photos = Photo.objects.all()
    username=request.user.id
    if post.author_id == username:
        post.delete()
    return render(request,'photo/list.html',{'photos':photos})



class PhotoUpdateView(LoginRequiredMixin,UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'
