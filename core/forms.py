from django.forms import widgets

class BootstrapFormMixin(object):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if (isinstance(field.widget, widgets.TextInput) or
                isinstance(field.widget, widgets.Textarea)):
                field.widget.attrs.update({
                    "class": "form-control",     
                })