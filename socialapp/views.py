from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from .models import Choice, Socialpost
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, SignInForm


class IndexView(generic.ListView):
    template_name = "socialapp/index.html"
    context_object_name = "latest_socialpost_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Socialpost.objects.order_by("-pub_date")[:200]

    @method_decorator(login_required(login_url='socialapp:signin'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DetailView(generic.DetailView):
    model = Socialpost
    template_name = "socialapp/detail.html"

    @method_decorator(login_required(login_url='socialapp:signin'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ResultsView(generic.DetailView):
    model = Socialpost
    template_name = "socialapp/results.html"

    @method_decorator(login_required(login_url='socialapp:signin'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def vote(request, socialpost_id):
    socialpost = get_object_or_404(Socialpost, pk=socialpost_id)
    try:
        selected_choice = socialpost.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "socialapp/detail.html",
            {
                "socialpost": socialpost,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("socialapp:results", args=(socialpost.id,)))


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('socialapp:index')
    else:
        form = SignUpForm()
    return render(request, 'socialapp/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('socialapp:index')
            else:
                messages.error(request, 'Wrong username or password entered.')
    else:
        form = SignInForm()

    return render(request, 'socialapp/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('socialapp:index')
