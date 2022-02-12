from django.db import models


class UploadFields(models.Model):
    """ Upload files model. """
    title = models.CharField(max_length=100)
    file = models.FileField(blank=True, null=True)


class FieldsFiles(models.Model):
    """ Fields files model. """
    upload_fields = models.ForeignKey(
        UploadFields,
        related_name='upload_fields',
        null=True,
        on_delete=models.PROTECT
    )
    buyer = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=18, decimal_places=2)
    amounts = models.IntegerField()
    address = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
