# theses/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Thesis
from .forms import *



@login_required
def thesis_list_view(request):
    if request.user.role == 'student':
        theses = Thesis.objects.filter(student=request.user)
    elif request.user.role == 'teacher':
        theses = Thesis.objects.filter(teacher=request.user)
    else:
        theses = Thesis.objects.all()
    return render(request, 'theses/thesis_list.html', {'theses': theses})



@login_required
def thesis_upload_view(request):
    if request.user.role != 'student':
        return redirect('dashboard')  # Only students can submit theses
    if request.method == 'POST':
        form = ThesisForm(request.POST, request.FILES)
        if form.is_valid():
            thesis = form.save(commit=False)
            thesis.student = request.user
            thesis.save()
            return redirect('dashboard')  # Redirect to student dashboard
    else:
        form = ThesisForm()
    return render(request, 'theses/thesis_upload.html', {'form': form})


# theses/views.py
@login_required
def thesis_review_list_view(request):
    if request.user.role != 'teacher':
        return redirect('home')  # Only teachers can access this view
    theses = Thesis.objects.filter(teacher=request.user, status='pending')
    return render(request, 'theses/thesis_review_list.html', {'theses': theses})

@login_required
def thesis_feedback_view(request, thesis_id):
    thesis = get_object_or_404(Thesis, id=thesis_id, teacher=request.user)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=thesis)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to dashboard after submission
    else:
        form = FeedbackForm(instance=thesis)
    return render(request, 'theses/thesis_feedback.html', {'form': form, 'thesis': thesis})

@login_required
def progress_list_view(request, thesis_id):
    thesis = get_object_or_404(Thesis, id=thesis_id)
    progress = ThesisProgress.objects.filter(thesis=thesis)
    if request.user != thesis.student and request.user != thesis.teacher:
        return redirect('dashboard')  # Unauthorized access redirects to dashboard
    return render(request, 'theses/progress_list.html', {'progress': progress, 'thesis': thesis})

@login_required
def progress_add_view(request, thesis_id):
    thesis = get_object_or_404(Thesis, id=thesis_id)
    if request.user.role != 'teacher' or request.user != thesis.teacher:
        return redirect('dashboard')  # Only teachers assigned to the thesis can add progress
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            milestone = form.save(commit=False)
            milestone.thesis = thesis
            milestone.save()
            return redirect('progress_list', thesis_id=thesis.id)
    else:
        form = ProgressForm()
    return render(request, 'theses/progress_add.html', {'form': form, 'thesis': thesis})




# theses/views.py
from django.db.models import Q

@login_required
def dashboard_view(request):
    if request.user.role == 'student':
        theses = Thesis.objects.filter(student=request.user)
        teachers = CustomUser.objects.filter(role='teacher')  # Fetch all teachers
        return render(request, 'theses/student_dashboard.html', {'theses': theses, 'teachers': teachers})
    elif request.user.role == 'teacher':
         # Show theses assigned to the teacher
        pending_theses = Thesis.objects.filter(teacher=request.user, status='pending')
        approved_theses = Thesis.objects.filter(teacher=request.user, status='approved')
        graded_theses = Thesis.objects.filter(teacher=request.user, grade__isnull=False)
        return render(request, 'theses/teacher_dashboard.html', {
            'pending_theses': pending_theses,
            'approved_theses': approved_theses,
            'graded_theses': graded_theses,
        })

    else:
        return render(request, 'theses/admin_dashboard.html')


@login_required
def thesis_progress_view(request, thesis_id):
    thesis = get_object_or_404(Thesis, id=thesis_id, student=request.user)
    progress = ThesisProgress.objects.filter(thesis=thesis)
    return render(request, 'theses/thesis_progress.html', {'thesis': thesis, 'progress': progress})
