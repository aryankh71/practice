from django import forms
from .models import Brand, Mobile


# class SignUp(forms.Form):
#     name = forms.CharField(max_length=100)
#     lastname = forms.CharField(max_length=100)
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=100)
#     email = forms.EmailField(required=False)
#
#     def clean_name(self):
#         name = self.cleaned_data['name']
#         is_valid = name[0].upper() == name[0]
#         if not is_valid:
#             raise forms.ValidationError(
#                 "your name should start with camel case letter"
#             )
#         return name


class ModelForm(forms.Form):
    model = forms.CharField(label='نام مدل')
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), label='برند')
    price = forms.IntegerField(label='قیمت')

    # class Meta:
    #     model = YourModel
    #     fields = ['photos']
    #
    # photos = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        brand = Mobile
        fields = {'name', 'nationality', 'photos'}
        photos = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': False}))

    def clean_model(self):
        model = self.cleaned_data['model']
        if not model[0].upper() == model[0]:
            raise forms.ValidationError(
                "your name should start with camel case letter"
            )
        if not len(model) <= 100:
            raise forms.ValidationError(
                "max length not valid"
            )
        return model

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 10000000:
            raise forms.ValidationError(
                "your price should be more than 1000000T!"
            )
        return price
