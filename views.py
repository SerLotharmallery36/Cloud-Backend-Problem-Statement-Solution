from django.shortcuts import render,get_object_or_404,redirect
from tablib import Dataset
from .resources import *
from .Forms import *
def simple_upload_Students(request):
    if request.method == 'POST':
        students_resource = StudentsResource()
        dataset = Dataset()
        new_students = request.FILES['StudentFile']

        if not new_students.name.endswith('xlsx' or 'csv'):
            messages.info(request,'wrong format')
            return render(request, 'Student_import.html')


        imported_data = dataset.load(new_students.read(),format='xlsx'or'csv')
       # result = students_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        students_resource.import_data(imported_data, dry_run=False)
        return redirect('../')
          # Actually import now
        #for data in imported_data:
            #value = Students(
             #   data)

    return render(request, 'Student_import.html')
# Create your views here.


def simple_upload_Schools(request):
    if request.method == 'POST':
        schools_resource = SchoolsResource()
        dataset = Dataset()
        new_schools = request.FILES['SchoolFile']
        if not new_students.name.endswith('xlsx' or 'csv'):
             messages.info(request,'wrong format')
             return render(request, 'School_import.html')




        imported_data = dataset.load(new_schools.read())
        #result = schools_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        schools_resource.import_data(imported_data, dry_run=False)
        return redirect('../')
          # Actually import now

    return render(request, 'School_import.html')


def simple_upload_Books(request):
    if request.method == 'POST':
        books_resource = BooksResource()
        dataset = Dataset()
        new_books = request.FILES['BookFile']

        if not new_bookss.name.endswith('xlsx' or 'csv'):
             messages.info(request,'wrong format')
             return render(request, 'Book_import.html')



        imported_data = dataset.load(new_books.read(),format='xlsx' or 'csv')
       # result = books_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        books_resource.import_data(import_data, dry_run=False)  # Actually import now
        return redirect('../')
    return render(request, 'Book_import.html',{})

def Import_view(request,*args,**kwargs):
    #file_import = File_import(request.POST or None)
    #context = {
     #   'files' : file_import,
    #} 
    return render(request, 'import.html',{})


def student_details_search_view(request,*args,**kwargs):
        my_form = Student_details_search()
        context = {
                'form' : my_form
        }

        return render(request, 'student_details_search.html',context)


def student_details_view(request,std_id,std_name):
        #s_id = getattr(get_object_or_404(StudentsResource,ID=std_id, first_name=std_name), 'ID'),
        std_fullname = getattr(get_object_or_404(Students,id=std_id, first_name=std_name), 'first_name') + " " +getattr(Students.objects.get(id=std_id, first_name=std_name), 'last_name')
        std_email = getattr(get_object_or_404(Students,id=std_id, first_name=std_name), 'email')
        std_gender = getattr(Students.objects.get(id=std_id, first_name=std_name), 'gender')
        std_schoolname = getattr(Students.objects.get(id=std_id, first_name=std_name), 'school')
        if std_schoolname== ' ':
            std_schoolphone=std_schoolname
        else:
            std_schoolphone = getattr(get_object_or_404(Schools,school=std_schoolname), 'phone')
        std_books = getattr(Students.objetcs.get(id=std_id, first_name=std_name), 'books')
        if std_books== ' ':
            std_pages=std_books
        else:
            std_pages = getattr(Books.objects.get(Title=std_books), 'Number_of_Pages')

        context = {

                'Student_ID' : std_id,
                'Student_Name' : std_fullname,
                'Gender' : std_gender,
                'School_Name' : std_schoolname,
                'School_Phone' : std_schoolphone,
                'Books' : std_books,
                'Total_Pages' : std_pages
        }

        return render(request, 'student_details.html',context)

   