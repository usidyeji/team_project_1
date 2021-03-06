from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Tag
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.core.exceptions import PermissionDenied


# Create your views here.
class PostList(ListView):
  model = Post
  ordering = '-pk'

class PostDetail(DetailView):
  model = Post

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['title', 'hook_text', 'content', 'file_upload']

  def form_valid(self, form):
    current_user = self.request.user
    if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
      form.instance.author = current_user
      response = super(PostCreate, self).form_valid(form)
      
      tags_str = self.request.POST.get('tags_str')
      if tags_str:
        tags_str = tags_str.strip()
        tags_str = tags_str.replace(',', ';')
        tags_list = tags_str.split(';')

        for t in tags_list:
          t = t.strip()
          tag, is_tag_created = Tag.objects.get_or_create(name=t)
          if is_tag_created:
            tag.slug = slugify(t, allow_unicode=True)
            tag.save()
          self.object.tags.add(tag)

      return response

      
    else:
      return redirect('/note/')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'file_upload']

    template_name = 'classnote/post_update_form.html'

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data()
        if self.object.tags.exists():
            tags_str_list = list()
            for t in self.object.tags.all():
                tags_str_list.append(t.name)
            context['tags_str_default'] = '; '.join(tags_str_list)

        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
      response = super(PostUpdate, self).form_valid(form)
      self.object.tags.clear() 
      
      tags_str = self.request.POST.get('tags_str')
      if tags_str:
        tags_str = tags_str.strip()
        tags_str = tags_str.replace(',', ';')
        tags_list = tags_str.split(';')

        for t in tags_list:
          t = t.strip()
          tag, is_tag_created = Tag.objects.get_or_create(name=t)
          if is_tag_created:
            tag.slug = slugify(t, allow_unicode=True)
            tag.save()
          self.object.tags.add(tag)

      return response     


# ?????? (????????? ???????????????)
def tag_page(request, slug):
  tag = Tag.objects.get(slug=slug)
  post_list = tag.post_set.all()
  return render(
    request,
    'classnote/post_list.html',
    {
      'post_list': post_list,
      'tag': tag,
    }
    )


