from django import forms
from .models import *
# from .models import ExtendedComment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ['model', 'stock']
        labels = {
            'model': 'نام کالا',
            'stock': 'موجودی انبار',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].initial = 1  # مقدار پیش‌فرض برای stock
# class InventoryForm(forms.ModelForm):
#     stock = forms.IntegerField(default=1, verbose_name='موجودی انبار')

# class ExtendedCommentForm(forms.ModelForm):
#     class Meta:
#         model = ExtendedComment
#         fields = ['comment_text']  # فیلدهای مورد نیاز خود را اضافه کنید
#
#     def __init__(self, *args, **kwargs):
#         self.content_type = kwargs.pop('content_type', None)
#         self.object_pk = kwargs.pop('object_pk', None)
#         super().__init__(*args, **kwargs)
#
#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         instance.content_types = self.content_type
#         instance.objects_pk = self.object_pk
#         if commit:
#             instance.save()
#         return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        # exclude = ('post', 'created', 'updated', 'active')


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, help_text='required.')
    last_name = forms.CharField(max_length=50, required=True, help_text='required.')
    email = forms.EmailField(max_length=200, help_text='required. Enter a valid email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


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


# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = ExtendedComment
#         fields = ['commented_by','comment']