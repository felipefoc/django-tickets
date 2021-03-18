from .models import Notification


class NotificationAndUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.notification = None
        self.user = None
       
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        return response

    def process_template_response(self, request, response):
        self.notification = Notification.objects.filter(owner=request.user, viewed=False).order_by('-date')
        self.user = request.user
        self.username = request.user.first_name
        
        response.context_data["notification"] = self.notification
        response.context_data["user"] = self.user
        response.context_data["username"] = self.username
        
        
        return response



 