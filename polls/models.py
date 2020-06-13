from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 我们的数据结构是在模型中定义的，模型是定义要存储在底层数据库中的字段的Python类。

# test
class MyModelName(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields 定义字段
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
    ...

    # Metadata 声明模型级别的元数据，控制在查询模型类型时返回的记录的默认排序
    class Meta: 
        ordering = ["-my_field_name"]

    # Methods ？？？这函数返回一个在网站上显示个人模型记录的URL
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
    #为每个对象返回一个人类可读的字符串。
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns
# Book 模型 一本可用的书的所有信息
class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    # 书的名称
    title = models.CharField(max_length=200)
    # 书的作者
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # 简介
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    # ISBN国际标准书号
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character ISBN number</a>')
    # 这是书的封面
    # cover = model.ImageField()
    # 这是库存数
    count = models.IntegerField()
    # 书的价格
    price = models.IntegerField()
    # 书的类型
    genre = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
	# 管理数据库站点
    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.title, self.author)

    '''
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    '''        
    # display_genre.short_description = 'Genre'

	
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])

# Author 模型
class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)

