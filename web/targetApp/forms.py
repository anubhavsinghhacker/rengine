from django import forms
from .models import Domain
from reNgine.validators import validate_domain


class AddTargetForm(forms.Form):
    name = forms.CharField(
        validators=[validate_domain],
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "domainName",
                "placeholder": "example.com"
            }
        ))
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "domainDescription",
            }
        ))

    def clean_name(self):
        data = self.cleaned_data['name']
        if Domain.objects.filter(name=data).count() > 0:
            raise forms.ValidationError("{} target/domain already exists".format(data))
        return data


class UpdateTargetForm(forms.ModelForm):
    class Meta:
        model = Domain
        fields = ['name', 'description']
    name = forms.CharField(
        validators=[validate_domain],
        required=True,
        disabled=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "domainName",
            }
        ))
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "id": "domainDescription",
            }
        ))

    def set_value(self, domain_value, description_value):
        self.initial['name'] = domain_value
        self.initial['description'] = description_value