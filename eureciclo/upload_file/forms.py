from django.forms import ModelForm
from .models import FieldsFiles, UploadFields


class FieldsFilesForm(ModelForm):
    """  Fields files form.  """

    class Meta:
        model = FieldsFiles

        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(FieldsFilesForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {
                'required': '{fieldname} required.'.format(fieldname=field.label)}


class UploadFieldsForm(ModelForm):
    """ Upload fields form. """

    class Meta:
        model = UploadFields

        fields = ['title', 'file']

    def __init__(self, *args, **kwargs):
        super(UploadFieldsForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {
                'required': '{fieldname} required.'.format(fieldname=field.label)}
