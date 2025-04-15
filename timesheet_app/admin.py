from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.admin import AdminSite
from import_export.admin import ExportMixin
from import_export import resources

from .models import (
    CustomUser, Region, Country, CostCentre, LocationCostCentre,
    StaffingCategory, StaffProfile, StaffDetails,
    AttendanceType, LTA, Rate, TimesheetEntry
)

# -----------------------------
# Custom AdminSite
# -----------------------------
class CustomAdminSite(admin.AdminSite):
    site_header = "INVOFLEET Admin Panel"
    site_title = "INVOFLEET Admin"
    index_title = "Welcome to INVOFLEET Admin Dashboard"

    def get_app_list(self, request, app_label=None):
        app_list = super().get_app_list(request, app_label)
        order = [
            'CustomUser', 'Region', 'Country', 'CostCentre',
            'LocationCostCentre', 'StaffingCategory', 'StaffProfile',
            'StaffDetails', 'AttendanceType', 'LTA', 'Rate', 'TimesheetEntry'
        ]
        for app in app_list:
            app['models'].sort(
                key=lambda x: order.index(x['object_name']) if x['object_name'] in order else 999
            )
        return app_list

admin_site = CustomAdminSite(name='myadmin')

# -----------------------------
# Resources for Import/Export
# -----------------------------
class CustomUserResource(resources.ModelResource):
    class Meta:
        model = CustomUser

class RegionResource(resources.ModelResource):
    class Meta:
        model = Region

class CountryResource(resources.ModelResource):
    class Meta:
        model = Country

class CostCentreResource(resources.ModelResource):
    class Meta:
        model = CostCentre

class LocationCostCentreResource(resources.ModelResource):
    class Meta:
        model = LocationCostCentre

class StaffingCategoryResource(resources.ModelResource):
    class Meta:
        model = StaffingCategory

class StaffProfileResource(resources.ModelResource):
    class Meta:
        model = StaffProfile

class StaffDetailsResource(resources.ModelResource):
    class Meta:
        model = StaffDetails

class AttendanceTypeResource(resources.ModelResource):
    class Meta:
        model = AttendanceType

class LTAResource(resources.ModelResource):
    class Meta:
        model = LTA

class RateResource(resources.ModelResource):
    class Meta:
        model = Rate

class TimesheetEntryResource(resources.ModelResource):
    class Meta:
        model = TimesheetEntry

# -----------------------------
# Admin Configs with Export
# -----------------------------
class CustomUserAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = CustomUserResource
    list_display = ('user_id', 'username', 'access_level', 'location', 'region')

class RegionAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = RegionResource
    list_display = ('region_id', 'region_desc')

class CountryAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = CountryResource
    list_display = ('country_id', 'country_desc', 'region')

class CostCentreAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = CostCentreResource
    list_display = ('costcenter_id', 'costcenter_desc', 'country', 'region')

class LocationCostCentreAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = LocationCostCentreResource
    list_display = ('location_costcentre_id', 'location_costcentre_desc', 'costcenter', 'country', 'region')

class StaffingCategoryAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = StaffingCategoryResource
    list_display = ('staffing_category_id', 'staffing_category_desc')

class StaffProfileAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = StaffProfileResource
    list_display = ('profile_id', 'profile_desc')

class StaffDetailsAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = StaffDetailsResource
    list_display = ('staff_id', 'staff_name', 'profile', 'region', 'country')

class AttendanceTypeAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = AttendanceTypeResource
    list_display = ('attendence_id', 'attendence_desc')

class LTAAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = LTAResource
    list_display = ('lta_number', 'lta_type', 'supplier_type', 'lta_start_date', 'lta_end_date')

class RateAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = RateResource
    list_display = ('id', 'profile', 'profile_desc', 'wage_rate_per_day', 'overnight_rate_per_day')

class TimesheetEntryAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = TimesheetEntryResource
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

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
