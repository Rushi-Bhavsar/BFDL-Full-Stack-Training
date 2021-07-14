from django import forms
from django.core import validators


# If we want to create custom validator, we need to create a function with parameter name = "value"
def custom_validator(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name must start with letter z")


class FirstForm(forms.Form):
    name = forms.CharField(validators=[custom_validator])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    # bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput)
    # # required=False will hide this bot_catcher field from the user. It will be present only in HTML
    # # file but it will be hidden from the user.
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])
    # If we want to use django built-in validator we need to add extra argument of validators to the field that we
    # want to validate.


    # # Whenever we want to create a custom form validator we need to create a function which start with
    # # word "clean_(field_name) which we want to validate."
    # def clean_bot_catcher(self):
    #     bot = self.cleaned_data['bot_catcher']
    #     if len(bot):
    #         raise forms.ValidationError("Haha.. Screw you bot.!!!")
    #     return bot

    # Django core build in validator.
