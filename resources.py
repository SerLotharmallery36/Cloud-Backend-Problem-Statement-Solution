from import_export import resources
from .models import *

class StudentsResource(resources.ModelResource):
    class meta:
        model = Students
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('ID', 'first_name', 'email')



class SchoolsResource(resources.ModelResource):
    class meta:
        model = Schools
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('school', 'email', 'phone')



class BooksResource(resources.ModelResource):
    class meta:
        model = Books
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('Title')