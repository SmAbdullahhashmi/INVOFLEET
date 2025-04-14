from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.shortcuts import render, redirect
from .forms import StaffForm, CustomUserForm
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
    return render(request, 'home.html')

@staff_member_required
def create_staff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_success')
    else:
        form = StaffForm()
    return render(request, 'create_staff.html', {'form': form})

@staff_member_required
def create_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_success')
    else:
        form = CustomUserForm()
    return render(request, 'create_user.html', {'form': form})

def staff_success(request):
    return render(request, 'success.html', {'message': 'Staff Created Successfully'})

def user_success(request):
    return render(request, 'success.html', {'message': 'User Created Successfully'})

from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
from .models import TimesheetEntry
from reportlab.pdfgen import canvas

# Admin view to display timesheet entries
@staff_member_required
def admin_timesheet_report(request):
    entries = TimesheetEntry.objects.select_related('staff').all().order_by('-date')
    return render(request, 'admin_timesheet_report.html', {'entries': entries})

# Export to Excel
@staff_member_required
def export_timesheet_excel(request):
    entries = TimesheetEntry.objects.select_related('staff').values(
        'date', 'staff__staff_name', 'location', 'present', 'time_in', 'time_out', 'overnight', 'cra'
    )
    df = pd.DataFrame(entries)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="timesheet_report.xlsx"'
    df.to_excel(response, index=False)
    return response

# Export to PDF using ReportLab
@staff_member_required
def export_timesheet_pdf(request):
    entries = TimesheetEntry.objects.select_related('staff').all().order_by('-date')
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="timesheet_report.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, 800, "Timesheet Report")

    y = 770
    for e in entries:
        line = f"{e.date} - {e.staff.staff_name} - {e.location} - {e.time_in} to {e.time_out}"
        p.setFont("Helvetica", 10)
        p.drawString(50, y, line)
        y -= 15

        if y < 50:
            p.showPage()
            y = 800
            p.setFont("Helvetica-Bold", 14)
            p.drawString(100, 800, "Timesheet Report")
            y -= 30

    p.showPage()
    p.save()
    return response

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # 👈 Go to dashboard if already logged in

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # 👈 Go to dashboard after login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import StaffDetails
from .forms import TimesheetEntryForm
from django import forms

@login_required
def submit_timesheet_entry(request):
    try:
        # Step 1: Get the staff record linked to the logged-in user
        staff = StaffDetails.objects.get(user=request.user)
    except StaffDetails.DoesNotExist:
        return HttpResponse("You are not linked to a staff profile.", status=403)

    if request.method == 'POST':
        form = TimesheetEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.staff = staff  # Step 2: Automatically assign this staff
            entry.save()
            return redirect('timesheet_report')  # Go to report page
    else:
        form = TimesheetEntryForm()
        # Step 3: Hide the staff field from users
        form.fields['staff'].widget = forms.HiddenInput()

    return render(request, 'submit_timesheet_entry.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import StaffDetails, TimesheetEntry

@login_required
def timesheet_report(request):
    try:
        staff = StaffDetails.objects.get(user=request.user)
        entries = TimesheetEntry.objects.filter(staff=staff).order_by('-date')
    except StaffDetails.DoesNotExist:
        return HttpResponse("You are not linked to a staff profile.", status=403)

    return render(request, 'timesheet_report.html', {'entries': entries})
