from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
  posts = Post.objects.all().order_by('-pk')

  return render(
    request, 'classnote/notes.html',
    {
      'posts': posts,
    }
  )

def single_post_page(request, pk):
  post = Post.objects.get(pk=pk)

  return render(
    request, 'classnote/single_note.html',
    {
      'post': post,
    }
  )
