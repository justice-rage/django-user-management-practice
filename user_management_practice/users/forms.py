from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    ''' Adds email to UserCreationForm '''
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)