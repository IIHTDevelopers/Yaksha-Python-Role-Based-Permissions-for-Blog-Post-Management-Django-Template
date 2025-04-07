from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import BlogPost

def blog_list(request):
    pass
    # """View all blog posts (accessible to everyone)"""
    # posts = BlogPost.objects.all()
    # return render(request, "blog_list.html", {"posts": posts})


def blog_detail(request, post_id):
    pass
    # """View a single blog post (accessible to everyone)"""
    # post = get_object_or_404(BlogPost, id=post_id)
    # return render(request, "blog_detail.html", {"post": post})



def blog_edit(request, post_id):
    pass
    # """Only staff can edit posts"""
    # post = get_object_or_404(BlogPost, id=post_id)

    # if request.method == "POST":
    #     post.title = request.POST.get("title")
    #     post.content = request.POST.get("content")
    #     post.save()
    #     return redirect("blog_list")

    # return render(request, "blog_edit.html", {"post": post})


