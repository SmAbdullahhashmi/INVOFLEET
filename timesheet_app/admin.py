from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.admin import AdminSite
from import_export.admin import ImportExportModelAdmin
from import_export import resources

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
        import_id_fields = ['user_id']

class RegionResource(resources.ModelResource):
    class Meta:
        model = Region
        import_id_fields = ['region_id']

class CountryResource(resources.ModelResource):
    class Meta:
        model = Country
        import_id_fields = ['country_id']

class CostCentreResource(resources.ModelResource):
    class Meta:
        model = CostCentre
        import_id_fields = ['costcenter_id']

class LocationCostCentreResource(resources.ModelResource):
    class Meta:
        model = LocationCostCentre
        import_id_fields = ['location_costcentre_id']

class StaffingCategoryResource(resources.ModelResource):
    class Meta:
        model = StaffingCategory
        import_id_fields = ['staffing_category_id']

class StaffProfileResource(resources.ModelResource):
    class Meta:
        model = StaffProfile
        import_id_fields = ['profile_id']

class StaffDetailsResource(resources.ModelResource):
    class Meta:
        model = StaffDetails

class AttendanceTypeResource(resources.ModelResource):
    class Meta:
        model = AttendanceType
        import_id_fields = ['attendence_id']

class LTAResource(resources.ModelResource):
    class Meta:
        model = LTA
        import_id_fields = ['lta_number']

class RateResource(resources.ModelResource):
    class Meta:
        model = Rate

class TimesheetEntryResource(resources.ModelResource):
    class Meta:
        model = TimesheetEntry

# -----------------------------
# Admin Configs with Import/Export and Filters
# -----------------------------
class CustomUserAdmin(ImportExportModelAdmin):
    resource_class = CustomUserResource
    list_display = [field.name for field in CustomUser._meta.fields]
    list_filter = [field.name for field in CustomUser._meta.fields if field.name != 'id']

class RegionAdmin(ImportExportModelAdmin):
    resource_class = RegionResource
    list_display = [field.name for field in Region._meta.fields]
    list_filter = [field.name for field in Region._meta.fields if field.name != 'id']

class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource
    list_display = [field.name for field in Country._meta.fields]
    list_filter = [field.name for field in Country._meta.fields if field.name != 'id']

class CostCentreAdmin(ImportExportModelAdmin):
    resource_class = CostCentreResource
    list_display = [field.name for field in CostCentre._meta.fields]
    list_filter = [field.name for field in CostCentre._meta.fields if field.name != 'id']

class LocationCostCentreAdmin(ImportExportModelAdmin):
    resource_class = LocationCostCentreResource
    list_display = [field.name for field in LocationCostCentre._meta.fields]
    list_filter = [field.name for field in LocationCostCentre._meta.fields if field.name != 'id']

class StaffingCategoryAdmin(ImportExportModelAdmin):
    resource_class = StaffingCategoryResource
    list_display = [field.name for field in StaffingCategory._meta.fields]
    list_filter = [field.name for field in StaffingCategory._meta.fields if field.name != 'id']

class StaffProfileAdmin(ImportExportModelAdmin):
    resource_class = StaffProfileResource
    list_display = [field.name for field in StaffProfile._meta.fields]
    list_filter = [field.name for field in StaffProfile._meta.fields if field.name != 'id']

class StaffDetailsAdmin(ImportExportModelAdmin):
    resource_class = StaffDetailsResource
    list_display = [field.name for field in StaffDetails._meta.fields]
    list_filter = [field.name for field in StaffDetails._meta.fields if field.name != 'id']

class AttendanceTypeAdmin(ImportExportModelAdmin):
    resource_class = AttendanceTypeResource
    list_display = [field.name for field in AttendanceType._meta.fields]
    list_filter = [field.name for field in AttendanceType._meta.fields if field.name != 'id']

class LTAAdmin(ImportExportModelAdmin):
    resource_class = LTAResource
    list_display = [field.name for field in LTA._meta.fields]
    list_filter = [field.name for field in LTA._meta.fields if field.name != 'id']

class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = [field.name for field in Rate._meta.fields]
    list_filter = [field.name for field in Rate._meta.fields if field.name != 'id']

class TimesheetEntryAdmin(ImportExportModelAdmin):
    resource_class = TimesheetEntryResource
    list_display = [field.name for field in TimesheetEntry._meta.fields]
    list_filter = [field.name for field in TimesheetEntry._meta.fields if field.name != 'id']

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