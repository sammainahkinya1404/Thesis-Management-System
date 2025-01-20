from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from theses.models import Thesis
from .models import Grade
from .forms import GradeForm

@login_required
def grade_list_view(request):
    if request.user.role != 'teacher':
        return redirect('dashboard')  # Only teachers can grade
    # Filter theses that are approved but not yet graded
    theses = Thesis.objects.filter(teacher=request.user, status='approved').exclude(grade__isnull=False)
    return render(request, 'grading/grade_list.html', {'theses': theses})

@login_required
def grade_thesis_view(request, thesis_id):
    thesis = get_object_or_404(Thesis, id=thesis_id, teacher=request.user)
    grade = Grade.objects.filter(thesis=thesis).first()  # Fetch existing grade if any
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)  # Bind existing grade if present
        if form.is_valid():
            grade = form.save(commit=False)
            grade.thesis = thesis
            grade.save()
            return redirect('dashboard')  # Redirect to dashboard after grading
    else:
        form = GradeForm(instance=grade)
    return render(request, 'grading/grade_thesis.html', {'form': form, 'thesis': thesis})
