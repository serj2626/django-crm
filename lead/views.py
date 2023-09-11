from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from .models import Lead
from .forms import AddLeadForm


@login_required
def add_lead(request):
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()
            messages.success(request, 'Клиент успено добавлен в базу данных!')
            return redirect('dashboard:home')
    form = AddLeadForm()
    return render(request, 'lead/add_lead.html', {'form': form})


class LeadUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Lead
    form_class = AddLeadForm
    # fields = ('name', 'email', 'description', 'priority', 'status',)
    success_url = reverse_lazy('leads:leads_list')
    success_message = 'Данные успешно обновлены!'
    template_name = 'lead/leads_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit lead'

        return context

    # def get_queryset(self):
    #     queryset = super(LeadUpdateView, self).get_queryset()
    #     team = self.request.user.profile.active_team
    #
    #     return queryset.filter(team=team, pk=self.kwargs.get('pk'))


class LeadsListView(ListView):
    model = Lead
    template_name = 'lead/leads_list.html'
    context_object_name = 'leads_list'


class LeadsDetailView(DetailView):
    model = Lead
    template_name = 'lead/leads_detail.html'
    context_object_name = 'lead'


class LeadDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Lead
    success_url = reverse_lazy('leads:leads_list')
    success_message = 'Клиент успешно удален!'
    # def get_queryset(self):
    #     queryset = super(LeadDeleteView, self).get_queryset()
    #     team = self.request.user.profile.active_team
    #
    #     return queryset.filter(team=team, pk=self.kwargs.get('pk'))

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)
