from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Haiku, Tanka
from .forms import TankaForm


class HaikuList(generic.ListView):
    model = Haiku
    queryset = Haiku.objects.order_by('-create_date')
    template_name = 'index.html'
    # paginate_by = 10


class HaikuDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Haiku.objects
        haiku = get_object_or_404(queryset, slug=slug)
        tankas = haiku.tankas.order_by('create_date')  # filter by approval
        liked = False
        if haiku.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "haiku_detail.html",
            {
                "haiku": haiku,
                "tankas": tankas,
                "tanka_added": False,
                "liked": liked,
                "tanka_form": TankaForm()
            },
        )
