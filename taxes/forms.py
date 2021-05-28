from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(allow_empty_file=True)

    def __init__(self, data=None, files=None):
        super().__init__(data=data, files=files)


class UrlForm(forms.Form):
    url = forms.CharField(label='Enter url', max_length=100)


class DataForm(forms.Form):
    url = forms.CharField(label='Enter available data value', max_length=100)
