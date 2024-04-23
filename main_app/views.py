import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student, Class, Photo
# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def careers(request):
    return render(request, 'careers.html')

@login_required
def students_index(request):
  students = Student.objects.filter(user=request.user)
  # Another query
  # students = request.user.student_set.all()
  return render(request, 'students/index.html', {
    'students': students
  })
def blog(request):
    return render(request, 'blog.html')

def login(request):
    return render(request, 'login.html')

@login_required
def students_detail(request, student_id):
  student = Student.objects.get(id=student_id)
  # First, create a list of the class ids that the student DOES have
  id_list = student.classes.all().values_list('id')
  # Query for the classes that the student doesn't have
  # by using the exclude() method vs. the filter() method
  classes_student_doesnt_have = Class.objects.exclude(id__in=id_list)
  return render(request, 'students/detail.html', {
    'student': student,
    'classes': classes_student_doesnt_have
  })

class StudentCreate(LoginRequiredMixin, CreateView):
  model = Student
  fields = ['name','contact_number', 'age']

  def form_valid(self, form):
    # self.request.user is the logged in user
    form.instance.user = self.request.user
    # Let the CreateView's form_valid method
    # do its regular work (saving the object & redirecting)
    return super().form_valid(form)

class StudentUpdate(LoginRequiredMixin, UpdateView):
  model = Student
  fields = ['contact_number', 'age']

class StudentDelete(LoginRequiredMixin, DeleteView):
  model = Student
  success_url = '/students'

class ClassList(LoginRequiredMixin, ListView):
  model = Class

class ClassDetail(LoginRequiredMixin, DetailView):
  model = Class

class ClassCreate(LoginRequiredMixin, CreateView):
  model = Class
  fields = '__all__'

class ClassUpdate(LoginRequiredMixin, UpdateView):
  model = Class
  fields = ['name', 'group']

class ClassDelete(LoginRequiredMixin, DeleteView):
  model = Class
  success_url = '/classes'

@login_required
def assoc_class(request, student_id, class_id):
  Student.objects.get(id=student_id).classes.add(class_id)
  return redirect('detail', student_id=student_id)

@login_required
def unassoc_class(request, student_id, class_id):
  Student.objects.get(id=student_id).classes.remove(class_id)
  return redirect('detail', student_id=student_id)  

@login_required
def add_photo(request, student_id):
  # photo-file maps to the "name" attr on the <input>
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # Need a unique "key" (filename)
    # It needs to keep the same file extension
    # of the file that was uploaded (.png, .jpeg, etc.)
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, student_id=student_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  return redirect('detail', student_id=student_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # Save the user to the db
      user = form.save()
      # Automatically log in the new user
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup template
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)