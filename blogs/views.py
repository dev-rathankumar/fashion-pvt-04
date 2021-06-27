from django.shortcuts import render,get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Category, Blog, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def blog(request, slug=None):
    blogs = Blog.objects.all().filter(status = 1).order_by('id')
    paginator = Paginator(blogs, 8)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    blog_count = blogs.count()
    context = {
    'blogs': paged_blogs,
    'blog_count': blog_count,
    }

    return render(request, 'blogs/blogs.html', context)


def blog_detail(request, category_slug, blog_slug):
    try:
        single_blog = Blog.objects.get(category__slug=category_slug, slug=blog_slug)
        blog = get_object_or_404(Blog, category__slug=category_slug, slug=blog_slug)
        comments = blog.comments.filter(is_active=True).order_by('-created_on')
        new_comment = None

        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            comments_count = comments.count()
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.user = request.user
                new_comment.blog_id = blog.id
                reply_id = request.POST.get('comment_id')
                comment_body = request.POST.get('comment_body')
                reply_qs =None
                if reply_id:
                    reply_qs = Comment.objects.get(id=reply_id)
                new_comment = Comment.objects.create(
                    user = request.user,
                    blog = blog,
                    comment_body = comment_body,
                    reply=reply_qs
                )
                new_comment.save()
                url = request.META.get('HTTP_REFERER')  # get last url
                return HttpResponseRedirect(url)

        else:
            comment_form = CommentForm()
            comments_count = comments.count()

    except Exception as e:
        raise e
    context = {
        'single_blog': single_blog,
        'blog': blog,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'comments_count':comments_count,



        }
    return render(request, 'blogs/blog_detail.html', context)
