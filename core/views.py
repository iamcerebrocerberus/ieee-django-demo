from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import FeedbackForm
from .models import Feedback


# @login_required
def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_thanks')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

# @login_required
def feedback_thanks(request):
    return render(request, 'thanks.html') 

@login_required
@user_passes_test(lambda u: u.is_staff)
@login_required
@user_passes_test(lambda u: u.is_staff)
def feedback_list(request):
    feedbacks = Feedback.objects.order_by('-submitted_at')
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks})

