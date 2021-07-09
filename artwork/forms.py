from django import forms
from .models import Artwork, Medium

class ArtworkForm(forms.ModelForm):

    class Meta:
        model = Artwork
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        mediums = Medium.objects.all()
        friendly_names = [(m.id, m.get_friedly_name()) for m in mediums]

        self.fields["medium"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "stripe-style-input"