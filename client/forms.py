from django import forms
from .models import *
from tinymce.widgets import TinyMCE
from django.forms.models import inlineformset_factory




PhoneFormset = inlineformset_factory(Client, Phone, fields=('phone',), can_delete=True, extra=1)

EmailFormset = inlineformset_factory(Client, Email, fields=('email',), can_delete=True, extra=1)


CreatePhoneFormset = inlineformset_factory(Client, Phone, fields=('phone',), can_delete=True, extra=4)

CreateEmailFormset = inlineformset_factory(Client, Email, fields=('email',), can_delete=True, extra=4)
