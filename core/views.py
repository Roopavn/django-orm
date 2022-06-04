from django.shortcuts import render
from .models import Student,Teacher
from django.db import connection
from django.db.models import Q
from django.db.models import Sum, Max, Min, Avg
from django.db.models import F
# Create your views here.

#find all data
def student_list(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request, 'core/output.html',{'post':posts})

#OR query
def student_list(request):

    posts = Student.objects.filter(surname__startswith='nareppa') | Student.objects.filter(surname__startswith='vijay')
   

    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request, 'core/output.html',{'post':posts})

'''def student_list(request):

    posts = Student.objects.filter(Q(surname__stratswith = 'nareppa') | Q(surname__startswith = 'vijay'))

    print(posts)
    print(posts.query)
    print(connection.queries)
    return render(request, 'core/output.html',{'post':posts})'''

# And query
def student_list(request):
    posts = Student.objects.filter(classroom=10) & Student.objects.filter(age=23)

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})
#Q objects
def student_list(request):
    posts = Student.objects.filter(Q(classroom=10) & Q(age=23))

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})

#UNION QUERY
def student_list(request):
    posts = Student.objects.all().values_list("firstname").union(Teacher.objects.all().values_list("firstname"))

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})

#NOT(exclude)
def student_list(request):
    posts = Student.objects.exclude(age=21)

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})


def student_list(request):
    posts = Student.objects.exclude(age=21) & Student.objects.exclude(firstname__startswith='kala')

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})


def student_list(request):
    posts = Student.objects.exclude(age__gt=23)

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})

def student_list(request):
    posts = Student.objects.filter(~Q(age__gt=23))

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})
# Select and output indivitual fields

def student_list(request):
    posts = Student.objects.filter(classroom=12).only('firstname')

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})

#RAW queries
def student_list(request):
    posts = Student.objects.all()

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})


#data = Student.objects.aggregate(sum=Sum('age'), max=Max('age'),min=Min('ratings_count'),avg=Avg('age'))

def student_list(request):
    posts = Student.objects.aggregate(sum=Sum('age'))

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})
#maximum
def student_list(request):
    posts = Student.objects.aggregate(max=Max('age'))

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})

#minimum
def student_list(request):
    posts = Student.objects.aggregate(min=Min('age'))

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})

#average
def student_list(request):
    posts = Student.objects.aggregate(avg=Avg('age'))

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})

# update

def student_list(request):
    posts = Student.objects.update(age=F('age')*2)

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'output.html',{'post':posts})
#Create
def student_list(request):
    posts = Student.objects.create(firstname='roopa3', surname='ajay2', age=26, classroom=7)

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})

#delete
def student_list(request):
    posts = Student.objects.filter(age__gt=26).delete()

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})

#descending and assending order

def student_list(request):
    posts = Student.objects.order_by('age')#ascending order

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})

# descending order
def student_list(request):
    posts = Student.objects.order_by('-age')

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})

#count
def student_list(request):
    posts = Student.objects.count()

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})

#indexing or slicing

def student_list(request):
    posts = Student.objects.all()[1:5]

    print(posts)
    print(connection.queries)
    print(posts.query)
    return render(request, 'core/output.html',{'post':posts})

