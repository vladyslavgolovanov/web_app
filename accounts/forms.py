from django.forms import ModelForm

from accounts.models import Profile, Publication


class ProfileBaseForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileAddForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class ModelFormWithFileField(ModelForm):
    class Meta:
        model = Publication
        fields ='__all__'
