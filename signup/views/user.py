from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, Http404, HttpResponse
from signup.models import CustomUser, RegistrationProfile
from signup.views import render_with_context
import signup.signals as signals

from utils import addToQueryString

def do_login(request, key):
    profile = RegistrationProfile.objects.get_user(key)
    if profile:
        user = authenticate(username=profile.user.email)
        login(request, user)
        signals.user_login.send(None, user=user)
    return HttpResponseRedirect("/")

def do_logout(request):
    logout(request)
    return HttpResponseRedirect("/")

def activate_user(request, key):
    profile = RegistrationProfile.objects.activate_user(key)
    error = notice = ""
    if not profile:
        error = "Sorry, that key was invalid"
    else:
        notice = "Thanks, you've successfully confirmed your email"
        user = authenticate(username=profile.user.email)
        login(request, user)
    context = {'error': error,
               'notice': notice}
    return HttpResponseRedirect(addToQueryString("/", context))

def user(request, id):
    from tasks.models import TaskUser # Import here to avoid circular dependency
    
    context = {}
    user = get_object_or_404(CustomUser, pk=id)
    context['profile_user'] = user
    context['activity'] = TaskUser.objects.\
        filter(user=user).\
        filter(user__can_cc=True).\
        filter(state__in=[TaskUser.States.started,TaskUser.States.completed]).\
        order_by('-date_modified').distinct()
    context['badges'] = user.badge_set.order_by('-date_awarded')
    return render_with_context(request,
                               'user.html',
                               context)

def email_reminder(request):
    messages = []
    if request.method == "POST":
        email = request.POST['email']
        
        user = None
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            messages.append("I couldn't find a user with email address %s" % email)
        else:
            profile = user.registrationprofile_set.get()
            profile.send_activation_email()
            messages.append("Activation email re-sent. Please check your %s inbox. If it isn't there, check your spam folders" % email)
        
    return render_with_context(request, "email_reminder.html", {})