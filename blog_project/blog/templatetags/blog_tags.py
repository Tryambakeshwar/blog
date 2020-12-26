from blog.models import Post
from django import template
register=template.Library()


# **************simple tag to retirn num of post published************************
@register.simple_tag
def total_posts():
    return Post.objects.count()

# ************************inclusion_tag to display latest post*******************
@register.inclusion_tag('blog/latest_post123.html')
def show_latest_posts():
    latest_posts = Post.objects.order_by('-publish')[:5]
    return {'latest_posts':latest_posts}
# ******************************simple_tag to displat the most commented post************
from django.db.models import Count
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

