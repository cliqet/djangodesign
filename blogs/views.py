import time

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render
from django.core.paginator import Paginator
from django.urls import reverse

from .models import Blog, Category
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

MONTH_LIST = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

MONTH_LIST_NAMES = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

def get_last_twelve_months():
    # get the last 12 months
    x = 12  # no. of months
    now = time.localtime()
    date_range = [time.localtime(time.mktime((now.tm_year, now.tm_mon - n, 1, 0, 0, 0, 0, 0, 0)))[:2] for n in range(x)]

    months = []  # list of last 12 months
    years = []   # year associated with the months

    for i in range(0, len(date_range)):
        month = date_range[i][1]
        year = date_range[i][0]
        months.append(MONTH_LIST[month])
        years.append(year)

    last_twelve_months = zip(months, years)

    return last_twelve_months

def home(request):
    blog_list = Blog.objects.all().order_by('-post_date')
    categories = Category.objects.all()
    last_months = get_last_twelve_months()

    paginator = Paginator(blog_list, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'categories': categories,
        'page_obj' : page_obj,
        'blogs' : blog_list,
        'last_months' : last_months,
        'paginator' : paginator
    }
    return render(request, 'blogs/home.html', context)


class BlogDetailView(DetailView):
    model = Blog


def month_view(request, month, year):
    blog_list = Blog.objects.filter(post_date__month=MONTH_LIST_NAMES[month], post_date__year=year).order_by('-post_date')
    categories = Category.objects.all()
    last_months = get_last_twelve_months()

    paginator = Paginator(blog_list, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs' : blog_list,
        'page_obj' : page_obj,
        'last_months' : last_months,
        'categories' : categories,
        'paginator': paginator
    }
    return render(request, 'blogs/home.html', context)


def category_view(request, category):
    blog_list = Blog.objects.filter(category__name=category).order_by('-post_date')
    categories = Category.objects.all()
    last_months = get_last_twelve_months()

    paginator = Paginator(blog_list, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs' : blog_list,
        'page_obj' : page_obj,
        'last_months' : last_months,
        'categories' : categories,
        'paginator': paginator
    }
    return render(request, 'blogs/home.html', context)


class AddPost(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['category', 'title', 'content', 'post_date']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        view_name = 'user_created_blog'
        return reverse(view_name)

# for all users to check blog posts of a specific user
def user_posts_view(request, username):
    blog_list = Blog.objects.filter(author__username=username).order_by('-post_date')
    categories = Category.objects.all()
    last_months = get_last_twelve_months()

    paginator = Paginator(blog_list, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs' : blog_list,
        'page_obj' : page_obj,
        'last_months' : last_months,
        'categories' : categories,
        'paginator': paginator
    }
    return render(request, 'blogs/home.html', context)


# for user to see all their blog posts
@login_required
def user_created_blog(request):
    blog_list = Blog.objects.filter(author__username=request.user.username).order_by('-post_date')
    categories = Category.objects.all()
    last_months = get_last_twelve_months()

    paginator = Paginator(blog_list, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs': blog_list,
        'page_obj': page_obj,
        'last_months': last_months,
        'categories': categories,
        'paginator': paginator
    }

    return render(request, 'blogs/user_created_blog.html', context)


@login_required
def user_created_blog_category_view(request, category):
    blog_list = Blog.objects.filter(category__name=category, author__username=request.user.username).order_by('-post_date')
    categories = Category.objects.all()
    last_months = get_last_twelve_months()

    paginator = Paginator(blog_list, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs' : blog_list,
        'page_obj' : page_obj,
        'last_months' : last_months,
        'categories' : categories,
        'paginator': paginator
    }
    return render(request, 'blogs/user_created_blog.html', context)


@login_required
def user_created_blog_month_view(request, month, year):
    blog_list = Blog.objects.filter(post_date__month=MONTH_LIST_NAMES[month], post_date__year=year,
                                    author__username=request.user.username).order_by('-post_date')
    categories = Category.objects.all()
    last_months = get_last_twelve_months()

    paginator = Paginator(blog_list, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs' : blog_list,
        'page_obj' : page_obj,
        'last_months' : last_months,
        'categories' : categories,
        'paginator': paginator
    }
    return render(request, 'blogs/user_created_blog.html', context)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['category', 'title', 'content', 'post_date']
    template_name = 'blogs/user_edit_blog.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        view_name = 'user_created_blog'
        return reverse(view_name)


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog

    def get_success_url(self):
        view_name = 'user_created_blog'
        return reverse(view_name)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False