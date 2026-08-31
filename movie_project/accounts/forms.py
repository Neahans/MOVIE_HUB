from django import forms
from django.contrib.auth.models import User
from .models import Movie,Profile


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]


    widgets={
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
    }


    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm:
            if password != password_confirm:
                raise forms.ValidationError(
                    "Passwords do not match."
                )

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(
            self.cleaned_data['password']
        )

        if commit:
            user.save()

        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]

class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model=Profile 
        fields=['profile_photo']


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'title',
            'poster',
            'description',
            'release_date',
            'actors',
            'rating',
            'category',
            'trailer_link'
        ]

        widgets = {
            'release_date': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'description': forms.Textarea(
                attrs={'rows': 5}
            ),
            'actors': forms.Textarea(
                attrs={'rows': 3}
            ),
        }