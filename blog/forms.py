from django import forms
from blog.models import Entry, Comment, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))  # NOQA
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))  # NOQA

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. \
                                            Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    username = forms.CharField(required=True,
                               max_length=25,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))  # NOQA
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))  # NOQA
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))  # NOQA

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')
    #     return self.cleaned_data

# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']


class PostForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'post']
    title = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))  # NOQA
    post = forms.CharField(max_length=2000,
                           required=True,
                           widget=forms.Textarea(attrs={'class': 'form-control'}))  # NOQA

#     def clean(self):
#         title = self.cleaned_data.get('title')
#         post = self.cleaned_data.get('post')
#         return self.cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

    text = forms.CharField(max_length=2000,
                           label="Comment",
                           required=True,
                           widget=forms.Textarea(attrs={'class': 'form-control'}))  # NOQA


#     def clean(self):
#         text = self.cleaned_data.get('text')
#         return self.cleaned_data

class UpdateEmailForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('email',)

    def clean(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.exclude(pk=self.instance.pk).get(email=email)
        except User.DoesNotExist:
            return self.cleaned_data
        raise forms.ValidationError("Sorry, that email already exists. \
                                        Please try again.")


class UpdateAboutForm(forms.ModelForm):
    about = forms.CharField(required=True,
                            widget=forms.Textarea(attrs={'class': 'form-control'}))  # NOQA

    class Meta:
        model = UserProfile
        fields = ('about',)
