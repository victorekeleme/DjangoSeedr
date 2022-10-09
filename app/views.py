from django.shortcuts import redirect, get_object_or_404
from .models import FileLink, Link
from .forms import MagnetLink
from django.views.generic import ListView
from django.urls import reverse_lazy, reverse
from .thread import DownloaderThread




# Create your views here.


class IndexListView(ListView):
    model = Link
    template_name = 'index_list.html'
    context_object_name = 'links'

    def post(self, request):
        form = MagnetLink(request.POST)
        m_link = form.save(commit=False)
        if form.is_valid():
            m_link.save()
            return redirect('search')


class CompleteListView(ListView):
    model = FileLink
    template_name = 'complete_list.html'
    context_object_name = 'completed'


def LinkDeleteView(request, id):
    m_link = get_object_or_404(Link, id=id)
    m_link.delete()
    return redirect(reverse('search'))

def StartDownload(request, id):
    m = Link.objects.get(id=id).m_link
    DownloaderThread(int(m)).start()
    return redirect(reverse('search'))

