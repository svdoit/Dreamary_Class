from django.shortcuts import render, redirect, get_object_or_404
from .models import Designer

# Create your views here.
def home(request):
    designers = Designer.objects.all()
    return render(request, 'home.html', {'designers' : designers})

def introduce(request):
    return render(request, 'introduce.html')

def detail(request, designer_id):
    designer = get_object_or_404(Designer, pk = designer_id)
    return render(request, 'detail.html', {'designer' : designer})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == "POST":
        post = Designer()

        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.description = request.POST['description']

        post.save()

        return redirect('detail', post.id)
        # 위의 코드가 return redirect('profile/' + str(pst.id)) 임!! 위의 코드처럼 쓰는 걸 더 추천한다고..
        # detail은 urls.py의 detail임

def delete(request, designer_id):
    post = get_object_or_404(Designer, pk = designer_id)
    post.delete()

    return redirect('home')