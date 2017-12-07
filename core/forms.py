from django.forms import widgets
from django import forms
from .models import MyUser, User

class BootstrapFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(BootstrapFormMixin, self).__init__(*args, **kwargs)

        for field in self.fields.values():
            if (isinstance(field.widget, widgets.TextInput) or
                isinstance(field.widget, widgets.Textarea)):
                field.widget.attrs.update({
                    "class": "form-control",     
                })


class MyUserForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = MyUser
        fields = (
            "nickname",
            "ucity",
        )