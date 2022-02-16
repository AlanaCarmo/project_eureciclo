from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File
from .models import UploadFields


class QuestionModelTests(TestCase):

    def test_upload(self):
        data = File(open('upload_file/file.txt', 'rb'))
        file = SimpleUploadedFile('file.txt',
                                  data.read(),
                                  content_type="multipart/form-data")

        title = 'test_test'
        response = UploadFields(100, file, title)
        response = response.save()
        self.assertEqual(response, None)
