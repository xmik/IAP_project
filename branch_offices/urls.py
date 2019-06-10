from django.urls import path
from branch_offices import views as branch_offices_views


urlpatterns = [
    path('branch_offices/', branch_offices_views.branch_offices_list),
    path('branch_offices/<int:pk>/', branch_offices_views.branch_offices_detail),
]