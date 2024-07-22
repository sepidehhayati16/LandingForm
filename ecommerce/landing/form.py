from django import forms

class LandingForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LandingForm, self).__init__(*args, **kwargs)
        for item in LandingForm.visible_fields(self):
            item.field.widget.attrs['class'] = 'form-control'
    name = forms.CharField(max_length=100)
    family = forms.CharField(max_length=100)