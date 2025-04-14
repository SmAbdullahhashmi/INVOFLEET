from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.admin import AdminSite

from .models import (
    CustomUser, Region, Country, CostCentre, LocationCostCentre,
    StaffingCategory, StaffProfile, StaffDetails,
    AttendanceType, LTA, Rate, TimesheetEntry
)

# -----------------------------
# Custom AdminSite
# -----------------------------
class CustomAdminSite(AdminSite):
    site_header = "INVOFLEET Admin Panel"
    site_title = "INVOFLEET Admin"
    index_title = "Welcome to INVOFLEET Admin Dashboard"

    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        # Sorting model order manually
        model_order = [
            'CustomUser', 'Region', 'Country', 'CostCentre', 'LocationCostCentre',
            'StaffingCategory', 'StaffProfile', 'StaffDetails', 'AttendanceType',
            'LTA', 'Rate', 'TimesheetEntry', 'User', 'Group'
        ]
        for app in app_list:
            app['models'].sort(key=lambda x: model_order.index(x['object_name']) if x['object_name'] in model_order else 999)
        return app_list

admin_site = CustomAdminSite(name='myadmin')

# -----------------------------
# Admin Configs
# -----------------------------
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'access_level', 'location', 'region')

class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_id', 'region_desc')

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_id', 'country_desc', 'region')

class CostCentreAdmin(admin.ModelAdmin):
    list_display = ('costcenter_id', 'costcenter_desc', 'country', 'region')

class LocationCostCentreAdmin(admin.ModelAdmin):
    list_display = ('location_costcentre_id', 'location_costcentre_desc', 'costcenter', 'country', 'region')

class StaffingCategoryAdmin(admin.ModelAdmin):
    list_display = ('staffing_category_id', 'staffing_category_desc')

class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_id', 'profile_desc')

class StaffDetailsAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'staff_name', 'profile', 'region', 'country')

class AttendanceTypeAdmin(admin.ModelAdmin):
    list_display = ('attendence_id', 'attendence_desc')

class LTAAdmin(admin.ModelAdmin):
    list_display = ('lta_number', 'lta_type', 'supplier_type', 'lta_start_date', 'lta_end_date')

class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'profile_desc', 'wage_rate_per_day', 'overnight_rate_per_day')

class TimesheetEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'date', 'present', 'time_in', 'time_out', 'overnight', 'cra')

# -----------------------------
# Register all models
# -----------------------------
admin_site.register(CustomUser, CustomUserAdmin)
admin_site.register(Region, RegionAdmin)
admin_site.register(Country, CountryAdmin)
admin_site.register(CostCentre, CostCentreAdmin)
admin_site.register(LocationCostCentre, LocationCostCentreAdmin)
admin_site.register(StaffingCategory, StaffingCategoryAdmin)
admin_site.register(StaffProfile, StaffProfileAdmin)
admin_site.register(StaffDetails, StaffDetailsAdmin)
admin_site.register(AttendanceType, AttendanceTypeAdmin)
admin_site.register(LTA, LTAAdmin)
admin_site.register(Rate, RateAdmin)
admin_site.register(TimesheetEntry, TimesheetEntryAdmin)

# ✅ Add built-in User & Group
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
