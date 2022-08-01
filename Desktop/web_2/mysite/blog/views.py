import json
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from . import models 
from . import forms


def index(req): 
    return HttpResponse('blog')

def post_list(req):
    # posts = [
    #     {'pk': 1, 'title': 'html', 'content': 'html is ...'},
    #     {'pk': 2, 'title': 'css', 'content': 'css is ...'},
    #     {'pk': 3, 'title': 'javascipt', 'content': 'javascipt is ...'},
    #     {'pk': 4, 'title': 'python', 'content': 'python is ...'},
    #     {'pk': 5, 'title': 'django', 'content': 'django is ...'},
    # ]
    posts = models.Post.objects.all()
    return render(req, 'blog/post_list.html', {"post_list": posts})
    # Create your views here.

def post_detail(req, pk):
    post = models.Post.objects.get(pk=pk)
    return render( req, 'blog/post_detail.html', {"post": post})


def post_create(req):
    if req.method == "POST":
        form = forms.PostModelForm(req.POST)
        if form.is_valid():
            form.save()
        return redirect("/blog/post_list/")
    else:
        form = forms.PostForm()

    return render(req, 'blog/post_create.html', {'form': form})

from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

#get 일때 지원함 
@csrf_exempt
def api_post_list(req):
    if req.method == 'GET':
        posts = models.Post.objects.all()
        return JsonResponse({"results": list(posts.values())})
    elif req.method == 'POST':
        body = json.loads(req.body.decode('utf-8'))
        p=models.Post(title=body['title'], content = body['content'])
        p.save()
        return JsonResponse({"results":model_to_dict(p)})
    else :
        return HttpResponse(status=405)


from django.forms.models import model_to_dict
@csrf_exempt
def api_post(req,pk):
    if req.method == 'GET':
        post = models.Post.objects.filter(pk=pk)
        if not post:
            return JsonResponse(status=404)
        return JsonResponse({"results": model_to_dict(post)})
    elif req.method == 'PUT':
        body = json.loads(req.body.decode('utf-8'))
        post = models.Post.objects.filter(pk=pk)
        if not post:
            return HttpResponse(status=404)
        p = post[0]
        p.title = body['title']
        p.content = body['content']
        p.save()
        return JsonResponse({"results": model_to_dict(p)})
    elif req.method == 'DELETE':
        post = models.Post.objects.filter(pk=pk)
        if not post:
            return HttpResponse(status=404)
        p = post[0]
        p.delete()
        return JsonResponse({"results": "ok"})
    else:
        return JsonResponse(status=405)

        #   post = models.Post(title=req.Post["title"], 
        #   content=req.models.Post['content'])

    # if req.method == "POST" :
    #     post = models.Post(title=req.Post["title"], content=req.models.Post
    #     ['content'])
    #     post.save()

    return render( req, 'blog/post_create.html', {'form':form})



# def post_form(req):
#     form = forms.PostForm
#         post = models.Post(title=req.Post["title"], content=req.models.Post
#         ['content'])
#         post.save()
#         return redirect("/blog/post_list/")

#     return render( req, 'blog/post_create.html')

  # print(form.cleaned_data)
            # post = models.Post(**form.cleaned_data) 