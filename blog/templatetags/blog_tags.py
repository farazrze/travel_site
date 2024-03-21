from django import template
from blog.models import Post,Category
register = template.Library()

@register.simple_tag(name='post')
def test():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=20):
    return value[:arg]

@register.inclusion_tag('blog/popularpost.html')
def popular():
    posts=Post.objects.filter(status=1)
    return {'posts':posts}


@register.inclusion_tag('blog/categories.html')
def postcategories():
    posts=Post.objects.filter(status=1)   
    categories=Category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}



