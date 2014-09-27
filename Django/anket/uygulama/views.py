from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import get_object_or_404,render
from django.utils import timezone

from uygulama.models import Poll,Choice

class IndexView(generic.ListView):
    template_name = 'uygulama_template/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.filter(
        pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'uygulama_template/detail.html'
    def get_queryset(self):
        return Poll.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'uygulama_template/results.html'

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'uygulama_template/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('uygulama:results', args=(p.id,)))

# Create your views here.
