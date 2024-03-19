from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag(name='post')
def test():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=20):
    return value[:arg]




