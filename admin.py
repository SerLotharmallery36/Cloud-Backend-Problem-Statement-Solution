from django.contrib import admin
from .models import Students,Schools,Books
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Students,Schools,Books)
class std_Admin(ImportExportModelAdmin):
	pass
