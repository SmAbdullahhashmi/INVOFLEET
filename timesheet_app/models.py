from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

# -----------------------------
# MASTER TABLES
# -----------------------------

class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    region_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.region_desc

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_desc = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.country_desc

class CostCentre(models.Model):
    costcenter_id = models.AutoField(primary_key=True)
    costcenter_desc = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.costcenter_desc

class LocationCostCentre(models.Model):
    location_costcentre_id = models.AutoField(primary_key=True)
    location_costcentre_desc = models.CharField(max_length=100)
    costcenter = models.ForeignKey(CostCentre, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.location_costcentre_desc

class StaffingCategory(models.Model):
    staffing_category_id = models.AutoField(primary_key=True)
    staffing_category_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.staffing_category_desc

class StaffProfile(models.Model):
    profile_id = models.AutoField(primary_key=True)
    profile_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.profile_desc

# -----------------------------
# USERS
# -----------------------------

class CustomUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    access_level = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

# -----------------------------
# STAFF DETAILS
# -----------------------------

class StaffDetails(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=100)
    staff_contact_address = models.TextField()
    staff_mobile = models.CharField(max_length=20)
    profile = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    profile_desc = models.CharField(max_length=100)
    location_costcentre = models.ForeignKey(LocationCostCentre, on_delete=models.CASCADE)
    costcenter = models.ForeignKey(CostCentre, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.staff_name

# -----------------------------
# ATTENDANCE TYPE
# -----------------------------

class AttendanceType(models.Model):
    attendence_id = models.AutoField(primary_key=True)
    attendence_desc = models.CharField(max_length=100)

    def __str__(self):
        return self.attendence_desc

# -----------------------------
# LTA
# -----------------------------

class LTA(models.Model):
    lta_number = models.CharField(max_length=100, primary_key=True)
    lta_type = models.CharField(max_length=100)
    supplier_type = models.CharField(max_length=100)
    supplier_desc = models.CharField(max_length=255)
    lta_start_date = models.DateField()
    lta_end_date = models.DateField()

    def __str__(self):
        return self.lta_number

# -----------------------------
# RATES
# -----------------------------

class Rate(models.Model):
    profile = models.ForeignKey(StaffProfile, on_delete=models.CASCADE)
    profile_desc = models.CharField(max_length=100)
    wage_rate_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    overnight_rate_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    overtime_rate_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    int_dsa_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    allowance_presidential_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    lta_number = models.CharField(max_length=100)
    lta_type = models.CharField(max_length=100)
    supplier_type = models.CharField(max_length=100)
    supplier_desc = models.CharField(max_length=255)

    def __str__(self):
        return f"Rates for {self.profile_desc}"

class TimesheetEntry(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=100)  # e.g., Kosti
    focal_person = models.CharField(max_length=100, null=True, blank=True)
    staff = models.ForeignKey(StaffDetails, on_delete=models.CASCADE)
    
    present = models.BooleanField(default=False)
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)
    overnight = models.BooleanField(default=False)
    cra = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.staff.staff_name} - {self.date}"
