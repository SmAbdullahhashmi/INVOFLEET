from django.urls import path
from . import views




from . import views
from django.urls import path

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.home, name='home'),

    # ✅ Custom admin views
    path('manage/create-staff/', views.create_staff, name='create_staff'),
    path('manage/create-user/', views.create_user, name='create_user'),
    path('manage/timesheet-report/', views.admin_timesheet_report, name='admin_timesheet_report'),
    path('manage/export-excel/', views.export_timesheet_excel, name='export_timesheet_excel'),
    path('manage/export-pdf/', views.export_timesheet_pdf, name='export_timesheet_pdf'),

    # ✅ User timesheet and login/logout
    path('timesheet/entry/', views.submit_timesheet_entry, name='submit_timesheet_entry'),
    path('timesheet/report/', views.timesheet_report, name='timesheet_report'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]


