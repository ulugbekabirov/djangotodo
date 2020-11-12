from django import forms
from django.forms import ModelForm
from django import forms
from .models import Task


class TaskForm(ModelForm):
    title = forms.CharField(max_length=40,
                            widget=forms.TextInput(
                                attrs={"type": "text", "class": "form-control",
                                       "placeholder": "Enter todo",
                                       "aria-label": "Todo", "aria-describedby": "add-btn",
                                       }
                            ))

    class Meta:
        model = Task
        fields = "__all__"
