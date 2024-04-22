from django.forms import ModelForm

class FeedingForm(ModelForm):
  class Meta:
    fields = ['meal']