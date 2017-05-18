from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from data_loader.models import DataSource, DataProvider, DataFlowSettings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from data_loader.forms import DataSourceCreateForm, DataSourceUpdateForm, DataFlowSettingsForm
from django.contrib import messages


class DataSourceListView(LoginRequiredMixin, ListView):
    login_url = '/customer/login/'
    model = DataSource
    template_name = 'datasource/datasource_list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class DataSourceCreateView(LoginRequiredMixin, CreateView):
    model = DataSource
    form_class = DataSourceCreateForm
    template_name = 'datasource/datasource_create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        data_source = form.save(commit=False)
        data_source.user = self.request.user
        data_source.data_provider_id = self.kwargs.get('provider_id')
        config_file = data_source.generate_config()
        result_code = data_source.process_data(config_file)
        if result_code == 0:
            messages.success(self.request, 'Data has been loaded successfully')
        else:
            messages.warning(self.request, 'Data loading has been failed')
        return super(DataSourceCreateView, self).form_valid(form)


class DataSourceUpdateView(LoginRequiredMixin, UpdateView):
    model = DataSource
    form_class = DataSourceCreateForm
    template_name = 'datasource/datasource_update.html'
    success_url = reverse_lazy('index')


class DataSourceDeleteView(LoginRequiredMixin, DeleteView):
    model = DataSource
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('index')


class DataProviderListView(LoginRequiredMixin, ListView):
    model = DataProvider
    # queryset = DataProvider.objects.all()
    template_name = 'datasource/data_providers_list.html'


class DataFlowSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = DataFlowSettings
    form_class = DataFlowSettingsForm
    success_url = reverse_lazy('index')
    template_name = 'settings.html'

    def get_object(self, queryset=None):
        settings, created = DataFlowSettings.objects.get_or_create(user=self.request.user)
        return settings