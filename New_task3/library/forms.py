from django import forms


class AuthorForm(forms.Form):
    name = forms.CharField()

    def clean_name(self):
        name = self.cleaned_data['name']

        if not name[0].upper() == name[0]:
            raise forms.ValidationError(
                "your name should start with a camel case letter"
            )
        if not len(name) <= 100:
            raise forms.ValidationError(
                "length is not valid"
            )

        # is_valid = name[0].upper() == name[0] and len(name) <= 100
        # if not is_valid:
        #     raise forms.ValidationError(
        #         "your name should start with a camel case letter"
        #     )

        return name