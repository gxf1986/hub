from django.http import Http404
from django.views.generic import TemplateView
from .auth import login_guest_user
from .storer import storers
from .models import Project

class FrontPageView(TemplateView):
    template_name = 'index.html'

class SignInView(TemplateView):
    template_name = 'signin.html'

class GalleryView(TemplateView):
    template_name = 'gallery.html'

    def dispatch(self, request, *args, **kwargs):
        return super(GalleryView, self).dispatch(request, *args, **kwargs)

    def get(self, request, **kwargs):
        return super(GalleryView, self).get(request, **kwargs)

    def post(self, request, **kwargs):
        if not 'address' in request.POST:
            raise Http404

        address = request.POST['address']

        try:
            proto, path = address.split("://")
            storer = storers[proto](path)
        except:
            raise Http404

        if storer.valid_path():
            if not request.user.is_authenticated:
                login_guest_user(request)

            _, p = Project.objects.get_or_create(creator=request.user, address=address)
