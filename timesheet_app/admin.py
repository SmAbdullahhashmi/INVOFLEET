from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    CustomUser, StaffDetails, TimesheetEntry,
    Region, Country, CostCentre, LocationCostCentre,
    StaffingCategory, StaffProfile, AttendanceType,
    LTA, Rate
)

# -----------------------
# CustomUser
# -----------------------
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'access_level', 'location', 'region')
    search_fields = ('username',)
    list_filter = ('access_level', 'region')

# -----------------------
# StaffDetails
# -----------------------
@admin.register(StaffDetails)
class StaffDetailsAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'staff_name', 'profile', 'region', 'country')
    search_fields = ('staff_name',)
    list_filter = ('region', 'country', 'profile')

# -----------------------
# TimesheetEntry
# -----------------------
@admin.register(TimesheetEntry)
class TimesheetEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'staff', 'date', 'present', 'time_in', 'time_out', 'overnight', 'cra')
    list_filter = ('date', 'location', 'present', 'overnight', 'cra')

# -----------------------
# Master Tables
# -----------------------

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_id', 'region_desc')
    search_fields = ('region_desc',)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_id', 'country_desc', 'region')
    search_fields = ('country_desc',)
    list_filter = ('region',)

@admin.register(CostCentre)
class CostCentreAdmin(admin.ModelAdmin):
    list_display = ('costcenter_id', 'costcenter_desc', 'country', 'region')
    list_filter = ('country', 'region')

@admin.register(LocationCostCentre)
class LocationCostCentreAdmin(admin.ModelAdmin):
    list_display = ('location_costcentre_id', 'location_costcentre_desc', 'costcenter', 'country', 'region')
    list_filter = ('region', 'country', 'costcenter')

@admin.register(StaffingCategory)
class StaffingCategoryAdmin(admin.ModelAdmin):
    list_display = ('staffing_category_id', 'staffing_category_desc')

@admin.register(StaffProfile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_id', 'profile_desc')

@admin.register(AttendanceType)
class AttendanceTypeAdmin(admin.ModelAdmin):
    list_display = ('attendence_id', 'attendence_desc')

@admin.register(LTA)
class LTAAdmin(admin.ModelAdmin):
    list_display = ('lta_number', 'lta_type', 'supplier_type', 'lta_start_date', 'lta_end_date')

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'profile_desc', 'wage_rate_per_day', 'overnight_rate_per_day')
    search_fields = ('profile_desc',)




