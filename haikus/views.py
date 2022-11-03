from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Q, Count
from django.views import generic, View
from django.http import HttpResponseRedirect
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
        tankas = haiku.tankas.order_by('create_date')
        tanka_count = Tanka.objects.filter(approved=True).count()
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
                "tanka_form": TankaForm(),
                "tanka_count": tanka_count
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Haiku.objects
        haiku = get_object_or_404(queryset, slug=slug)
        tankas = haiku.tankas.order_by('create_date')  # filter by approval
        liked = False
        if haiku.likes.filter(id=self.request.user.id).exists():
            liked = True

        tanka_form = TankaForm(data=request.POST)

        if tanka_form.is_valid():
            tanka_form.instance.email = request.user.email
            tanka_form.instance.name = request.user.username
            tanka = tanka_form.save(commit=False)
            tanka.post = haiku
            tanka.save()
        else:
            tanka_form = TankaForm()

        return render(
            request,
            "haiku_detail.html",
            {
                "haiku": haiku,
                "tankas": tankas,
                "tanka_added": True,
                "tanka_form": tanka_form,
                "liked": liked,
            },
        )


class HaikuLike(View):

    def post(self, request, slug):
        haiku = get_object_or_404(Haiku, slug=slug)

        if haiku.likes.filter(id=request.user.id).exists():
            haiku.likes.remove(request.user)
        else:
            haiku.likes.add(request.user)

        return HttpResponseRedirect(reverse('haiku_detail', args=[slug]))
