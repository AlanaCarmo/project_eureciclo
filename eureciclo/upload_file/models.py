from django.db import models
import os
from django.core.exceptions import ValidationError


class UploadFields(models.Model):
    """ Upload files model. """

    def validate_file(self):
        """ Function to validate file format. """

        ext = os.path.splitext(self.name)[1]
        valid_extensions = ['.txt']
        if not ext.lower() in valid_extensions:
            raise ValidationError(u'Unsupported file extension.')

    title = models.CharField(unique=True,
                             max_length=100,
                             blank=False, null=False)
    file = models.FileField(upload_to='uploads', blank=False, null=False,
                            validators=[validate_file])
    date_created = models.DateTimeField(auto_now_add=True)


class FieldsFiles(models.Model):
    """ Fields files model. """

    upload_fields = models.ForeignKey(
        UploadFields,
        related_name='upload_fields',
        null=True,
        on_delete=models.PROTECT
    )
    buyer = models.CharField(
        max_length=100,
        blank=False,
        null=False)
    description = models.CharField(
        max_length=200,
        blank=False,
        null=False)
    price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        blank=False,
        null=False)
    amounts = models.IntegerField(
        blank=False,
        null=False)
    address = models.CharField(
        max_length=100,
        blank=False,
        null=False)
    supplier = models.CharField(
        max_length=100,
        blank=False,
        null=False)
