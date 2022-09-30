from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify

from app.community.models import UserCommunity
from .models import Post, Comment, Tag

from django.views.generic import View
# Create your views here.


def get_tags():
    tags = Tag.objects.all()
    return list(tags)

def get_user_communities(request):
        user_communities_relation = list(
            UserCommunity.objects.filter(user_id=request.user.id))
        my_communities = [item.community for item in user_communities_relation]
        return my_communities

def get_community_posts(request):
    communities = get_user_communities(request)
    communities_ids = [item.id for item in communities]
    posts = list(Post.objects.filter(community_id__in=communities_ids))
    posts = get_post_comments(posts)
    return posts

def get_post_comments( posts):
    for post in posts:
        post_comments = list(post.comment_set.all())
        post.comments = post_comments
        post.total_comments = len(post_comments)
    return posts


class HomeView(View):
    def get_context(self, request):
        posts = get_community_posts(request)
        tags = get_tags()
        context = {
            "logged_in": request.user.is_authenticated,
            "posts": posts,
            "tags": tags
        }
        return context

    def get(self, request):
        context = self.get_context(request)

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('signin'))
        return render(request, "post/home.html", context)

    def post(self, request):
        context = self.get_context(request)
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('signin'))
        return render(request, "post/home.html", context)


def add_comment(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('signin'))

    if request.method == "POST":
        post_id = request.POST['post_id']
        user_id = request.user.id
        text = request.POST['text']

        Comment.objects.create(text=text, post_id=post_id, user_id=user_id)

    return redirect('home')


class CreatePostView(View):
    def get_user_communities(self, request):
        user_communities_relation = list(
            UserCommunity.objects.filter(user_id=request.user.id))
        my_communities = [item.community for item in user_communities_relation]
        return my_communities

    def get(self, request):
        communities = self.get_user_communities(request)
        tags = get_tags()
        return render(request, 'post/create_post.html', {
            "communities": communities,
            "logged_in": request.user.is_authenticated,
            "tags": tags
        })

    def post(self, request):
        community_id = request.POST["community_id"]
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['image']
        slug = slugify(title)
        tags = request.POST.getlist('tag_id')
        tag_objs = Tag.objects.filter(id__in=tags)
        try:
            post = Post.objects.create(title=title, community_id=community_id,
                                       author_id=request.user.id, content=content, image=image, slug=slug)
            for obj in tag_objs.iterator():
                post.tags.add(obj)
            post.save()
        except Exception as e:
            print(e)
            return redirect('create-post')
        return redirect('home')


def tag_filter(request, id):
    tag_id = id
    all_posts = get_community_posts(request)

    tag_posts = []

    for post in all_posts:
        post_tags = list(post.tags.all())
        for post_tag in post_tags:
            if tag_id == post_tag.id:
                tag_posts.append(post)
                break

    tags = get_tags()
    context = {
        "logged_in": request.user.is_authenticated,
        "posts": tag_posts,
        "tags": tags
    }


    return render(request,"post/home.html",context)
