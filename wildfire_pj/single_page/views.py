from django.shortcuts import render
# from blog.models import Post

# Create your views here.
def mainpage(request):
  # recent_posts = Post.objects.order_by('-pk')[:3]
  return render (
    request, 'single_page/mainpage.html'
    )
  
def about_me(request):
  return render (
    request, 'single_page/about_me.html'
    )