
from django.http import HttpResponseForbidden

ALLOWED_IPS = ["123.45.67.89", "987.56.65.21", "127.0.0.1"]

class IPBlockingMIddleware:
    def get_client_ip(self, request):
        x_forward_for = request.META.get('HTTP_X_FORWARD_FOR')
        if x_forward_for:
            ip = x_forward_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            return ip
        
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        ip = self.get_client_ip(request)
        print(ip)
        if ip in ALLOWED_IPS:
            return HttpResponseForbidden("Forbidden: Your IP is blocked.")
        
        return self.get_response(request)
