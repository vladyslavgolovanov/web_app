from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponseRedirect, HttpResponseNotFound

from django.db.models import Q
from django.shortcuts import render

from accounts.forms import ProfileAddForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from accounts.forms import ProfileAddForm
from accounts.models import Profile


class ProfilesListView(ListView):
    model = Profile
    template_name = 'profiles/profiles.html'
    context_object_name = 'result'

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            qs = qs.filter(Q(nickname__icontains=search) | Q(login__icontains=search))
        return qs


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile.html'
    context_object_name = 'profile'
    pk_url_kwarg = 'item_id'


class ProfileCreateView(PermissionRequiredMixin, CreateView):
    model = Profile
    template_name = 'profiles/profile_add.html'
    form_class = ProfileAddForm
    permission_required = ('accounts.add_profile', )

    def get_success_url(self):
        return reverse('accounts:list')


def edit_profile(request, slug):
    try:
        profile = Profile.objects.get(id=slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Profile id {slug} not found')
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/profiles/show/{slug}')

    elif request.method == 'GET':
        form = ProfileEditForm(instance=profile)

    return render(
        request,
        template_name='profiles/profile_edit.html',
        context={
            'form': form
        }
    )
