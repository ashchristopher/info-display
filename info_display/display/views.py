from django.views.generic import TemplateView

class HomeView(TemplateView):

    template_name = 'display/home.html'

    def get(self, request):
        return self.render_to_response({})
