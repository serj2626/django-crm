from django.urls import path
from .views import add_lead, LeadsListView, LeadsDetailView, LeadDeleteView, LeadUpdateView,ConvertToClientView

app_name = 'leads'

urlpatterns = [

    path('', LeadsListView.as_view(), name='leads_list'),
    path('add-lead/', add_lead, name='add_lead'),
    path('<int:pk>/', LeadsDetailView.as_view(), name='leads_detail'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='leads_delete'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='leads_update'),
    path('<int:pk>/convert/', ConvertToClientView.as_view(), name='convert'),

]
