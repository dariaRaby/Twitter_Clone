from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    # If the method is POST
    form = PostForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #If the form is valid
        if form.is_valid():
            #yes, Save
            form.save()

            #Redirect to Home
            return HttpResponseRedirect('/')

        else:
            #no, Show Error
            return HttpResponseRedirect(form.errors.as_json())



    #get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    form = PostForm

    #show 
    return render(request, 'posts.html',
                    {'posts' : posts})

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')


# Edit Function
def edit(request, post_id):
    post= Post.objects.get(id=post_id)

    
    
    if request.method =='POST':
        form=PostForm(request.POST, request.FILES, instance= post )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect(form.errors.as_json())

    form = PostForm
    return render(request, "edit.html", {"post":post, 'form': form})


def Like(request, post_id):
    post = Post.objects.get(id=post_id)
    new_value = post.likes +1
    post.likes =new_value
    post.save()
    return HttpResponseRedirect('/')
