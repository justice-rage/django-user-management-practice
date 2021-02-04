from django.contrib.auth import UserCreationForm

class CustomCreationForm(UserCreationForm):
    """ Adds email to UserCreationForm """
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)