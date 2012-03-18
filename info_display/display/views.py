from django.views.generic import TemplateView

from display.models import MainMessage
from display.mixins import JSONResponseMixin


class HomeView(TemplateView):

    template_name = 'display/home.html'

    def get(self, request):
        try:
            main_message = MainMessage.objects.latest('date_added')
        except MainMessage.DoesNotExist:
            main_message = None
 
        context = {
            'total_subscribers' : getattr(main_message, 'message', 'No Data')
        }
 
        return self.render_to_response(context)


class JSONView(JSONResponseMixin, HomeView):
    
    template_name = None
