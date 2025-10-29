from django.shortcuts import render
from .models import Post

# Create your views here.
def list_posts_view(request):
    
    # get a list of posts from the database
    p = Post.objects.all()
    # print("Posts:", len(posts))
    # print("First Post", posts[0])
    c = {'posts': p}
    return render(request, 'post_list.html', c)
