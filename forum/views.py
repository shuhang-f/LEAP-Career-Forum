# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Discussion, Comment
from .forms import DiscussionForm


from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

# Not working rn

# def login_required_message(function):
#     def test_func(user):
#         if user.is_authenticated:
#             return True
#         messages.warning(user, 'Please log in to continue.')
#         return False

#     return user_passes_test(test_func, login_url='/login/', redirect_field_name=None)(function)

@login_required
def forum_list(request):
    discussions = Discussion.objects.all()
    
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            new_discussion = form.save(commit=False)
            new_discussion.author = request.user
            new_discussion.save()
            return redirect('/forum/')
    else:
        form = DiscussionForm()

    context = {
        'discussions': discussions,
        'form': form,
    }
    return render(request, 'forum_list.html', context)

def discussion_detail(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    comments = Comment.objects.filter(discussion=discussion).order_by('created_at')
    return render(request, 'discussion_detail.html', {'discussion': discussion, 'comments': comments})
