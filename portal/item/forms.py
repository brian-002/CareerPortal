from django import forms

from.models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields=('department', 'job_category', 'name', 'description', 'available', 'deadline', 'requirement', 'duties', 'created_by' )
        widgets = {
        'department':forms.Select(attrs={
            'class': INPUT_CLASSES
        }),
        'job_category':forms.Select(attrs={
            'class': INPUT_CLASSES
        }),
        'name':forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
        'description':forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),
        'deadline':forms.DateTimeInput(attrs={
            'class': INPUT_CLASSES
        }),
        'requirement':forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),
        'duties':forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),
        'created_by':forms.Select(attrs={
            'class': INPUT_CLASSES
        }),

    }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields=('name', 'description', 'available', 'deadline', 'requirement', 'duties' )
        widgets = {

        'name':forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
        'description':forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),
        'deadline':forms.DateTimeInput(attrs={
            'class': INPUT_CLASSES
        }),
        'requirement':forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),
        'duties':forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),


    }

    