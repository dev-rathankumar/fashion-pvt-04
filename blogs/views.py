from django.shortcuts import render,get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Category
from .forms import CommentForm
from .models import Blog,Category
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q


def blog(request, slug=None):
    categories = None
    blogs =None
    paged_blogs=None
    blog_count =0
    blogs = Blog.objects.filter(status=1).order_by('created_on')
    category = Category.objects.all()

    blogs = Blog.objects.all().filter(status = 1).order_by('id')
    recent_blogs = blogs.filter(status = 1).order_by('-id')[:2]
    paginator = Paginator(blogs, 8)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    blog_count = blogs.count()



    if slug != None:
        categories = get_object_or_404(Category, slug=slug).get_descendants(include_self=True)
        recent_blogs = blogs.filter(status = 1).order_by('-id')[:2]
        cblogs = Blog.objects.filter(category__in=categories)
        paginator = Paginator(cblogs, 8)
        page = request.GET.get('page')
        paged_blogs = paginator.get_page(page)
        blog_count = cblogs.count()


    if 'keyword' in request.GET: #?keyword=politics
        keyword = request.GET['keyword']
        if keyword:
            blogs = blogs.filter(Q(title__icontains=keyword) | Q(blog_body__icontains=keyword) | Q(short_description__icontains=keyword))
            recent_blogs = blogs.filter(status = 1).order_by('-id')[:2]
            paginator = Paginator(blogs, 8)
            page = request.GET.get('page')
            paged_blogs = paginator.get_page(page)
            blog_count = blogs.count()


    context = {
    'blogs': paged_blogs,
    'blog_count': blog_count,
    'category': category,
    'values' : request.GET,
    'recent_blogs' : recent_blogs,
    
    }

    return render(request, 'blogs/blogs.html', context)

@login_required(login_url = 'userLogin')
def blog_detail(request, category_slug, blog_slug):
    try:
        single_blog = Blog.objects.get(category__slug=category_slug, slug=blog_slug)
        comments = single_blog.comments.filter(is_active=True)
        new_comment = None
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            comments_count = comments.count()
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.user = request.user
                new_comment.blog = blog
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
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'comments_count':comments_count,


        }
    return render(request, 'blogs/blog_detail.html', context)
