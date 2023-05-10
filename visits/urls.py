from django.urls import path
from visits.views import *

urlpatterns = [
    path('', visit, name="get_list_or_post_visit"),
    path('<int:id>', visit_detail, name="delete_visit")
]
