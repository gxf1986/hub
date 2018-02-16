from django.http import Http404
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .auth import login_guest_user
from .storer import storers
from .models import Project, Cluster

class FrontPageView(TemplateView):
    template_name = 'index.html'

class SignInView(TemplateView):
    template_name = 'signin.html'

class GalleryView(ListView):
    template_name = 'gallery.html'
    model = Project

    def get_queryset(self):
        return Project.objects.filter(gallery=True)[:12]

    def post(self, request, **kwargs):
        if not 'address' in request.POST:
            raise Http404

        address = request.POST['address']

        try:
            proto, path = address.split("://")
            storer = storers[proto](path)
            assert(storer.valid_path())
            valid = True
        except:
            valid = False

        if valid:
            if not request.user.is_authenticated:
                login_guest_user(request)

            response = Project.open(user=request.user, address=address)
            # Redirect?

        self.object_list = self.get_queryset()
        return render(request, self.template_name, self.get_context_data())