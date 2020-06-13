from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

# 每一个“view”函数（请求的处理者）接受一个包含请求信息的HttpRequest对象，并且被要求返回一个包含格式化输出的HttpResponse（在下面的例子中是一个字符串）。
# 处理请求

from django.contrib.auth.decorators import login_required
from .models import Book, Author
@login_required
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_authors':num_authors},
    )

@login_required
def hello(request):
	return HttpResponse('22222')


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
# 通用视图将查询数据库，以获取指定模型（Book）的所有记录
class BookListView(LoginRequiredMixin,generic.ListView):
    model = Book
    paginate_by = 10

class BookDetailView(LoginRequiredMixin,generic.DetailView):
    model = Book


class AuthorListView(LoginRequiredMixin,generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(LoginRequiredMixin,generic.DetailView):
    model = Author

'''
from django.contrib.auth.mixins import LoginRequiredMixin
# 我的图书视图
class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    template_name ='polls/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
'''
