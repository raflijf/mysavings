from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Saving, SavingLogs
from  .forms import SavingLogsForm
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
class HomeView(LoginRequiredMixin, ListView) :
    template_name = 'main/home.html'
    context_object_name = 'savings'

    def get_queryset(self):
        return self.request.user.saving.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class CreateSavingView(LoginRequiredMixin, CreateView) :
    template_name = 'main/saving_form.html'
    model = Saving
    fields = ['description', 'target', 'title', 'deadline', 'collected']
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Tabungan berhasil dibuat')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        context['title_template'] = 'Buat tabungan'
        context['button_name'] = 'Buat'
        return context


class DetailSavingView(LoginRequiredMixin, FormMixin, DetailView) :
    template_name = 'main/detail_saving.html'    
    model = Saving
    form_class = SavingLogsForm

    def form_valid(self, form, status, nominal):
        form.instance.saving = self.get_object()
        form.instance.status = status
        if status == 'Masuk' :
            form.instance.total = self.get_total_nominal() + nominal 
        elif status == 'Keluar' :
            if self.get_total_nominal() - nominal > 0 :
                form.instance.total = self.get_total_nominal() - nominal
            else :
                form.instance.total = 0
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        logs = self.get_object().saving_entries.all()
        context = super().get_context_data(**kwargs)
        context['logs'] = logs
        context['collected'] = self.get_total_nominal()
        context['status'] = logs.order_by('-datetime').first() 
        context['gap'] = self.get_object().target - self.get_total_nominal()
        return context 

    def post(self, request, *args, **kwargs) :
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid() :
            action = self.request.POST.get('action')
            nominal = int(self.request.POST.get('nominal'))
            if action == 'setor' : 
                return self.form_valid(form, 'Masuk', nominal)
            else : 
                return self.form_valid(form, 'Keluar', nominal)
        else : 
            return self.form_invalid(form)
        
    # Custom Method 
    def get_total_nominal(self) :
        count = 0
        saving = self.get_object()
        count = saving.collected    
        for nominal in saving.saving_entries.all() : 
            if nominal.status == 'Masuk' :
                count += nominal.nominal
            elif nominal.status == 'Keluar' : 
                count -= nominal.nominal
                if count < 0 :
                    count = 0
        return count 
    
    def get_success_url(self):
        self.success_url = reverse_lazy('main:detail_saving', kwargs = {'slug' : self.kwargs['slug']})
        return super().get_success_url()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['saving'] = self.get_object()
        kwargs['collected'] = self.get_total_nominal()
        return kwargs

class UpdateSavingVIew(LoginRequiredMixin, UpdateView) :
    model = Saving
    fields = ['description', 'target', 'title', 'deadline']
    template_name = 'main/saving_form.html'
    
    def get_success_url(self):
        self.success_url = reverse_lazy('main:detail_saving', kwargs = {'slug' : self.kwargs['slug']})
        return super().get_success_url()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_name'] = 'Selesai'
        context['title_template'] = 'Edit tabungan'
        return context

class DeleteSavingView(LoginRequiredMixin, DeleteView) :
    model = Saving
    success_url = reverse_lazy('main:home')

