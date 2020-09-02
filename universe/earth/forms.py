from django import forms

from .models import Human


class HumanForm(forms.ModelForm):

    class Meta:
        model = Human
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["birthday"].widget = forms.DateInput(format=['%Y-%m-%d', '%Y/%m/%d'])
