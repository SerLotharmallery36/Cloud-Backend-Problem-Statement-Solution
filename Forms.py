from django import forms


class Student_details_search(forms.Form):
	Student_id = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder" : "Enter a valid Student ID"})) 
	Student_Name = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Enter the First Name of Student"}))
	


#class File_import(forms.Form):
#	Students_File = forms.FileField(widgets=forms.FileInput(attrs={"placeholder" : "Enter your Students File"}))
#	Schools_File = forms.FileField(widgets=forms.FileInput(attrs={"placeholder" : "Enter your Schools File"}))
#	Books_File = forms.FileField(widgets=forms.FileInput(attrs={"placeholder" : "Enter your Books File"}))