from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Socialpost


class IndexView(generic.ListView):
    template_name = "socialapp/index.html"
    context_object_name = "latest_socialpost_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Socialpost.objects.order_by("-pub_date")[:200]


class DetailView(generic.DetailView):
    model = Socialpost
    template_name = "socialapp/detail.html"


class ResultsView(generic.DetailView):
    model = Socialpost
    template_name = "socialapp/results.html"


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
