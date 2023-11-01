from django.urls import path
from .views import index, attedance_detail,attedance_take, attendance_update

urlpatterns = [
    path('', index),
    path('<int:team_id>/attendance/', attedance_detail, name="detail"),
    path('<int:team_id>/attendance/take/', attedance_take, name='take'),
    path('<int:attendance_id>/attendance/update/', attendance_update, name='update'),
    
]
