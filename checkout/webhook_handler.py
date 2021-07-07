from django.http import HttpResponse


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle generic/unknown/unexpected event
        """
        return HttpResponse(
            content = f"Unhandled Webhook Received: {event['type']}", 
            status = 200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment intent succeded event
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content = f"Webhook Received: {event['type']}", 
            status = 200)   

    def handle_payment_intent_failed(self, event):
        """
        Handle payment intent failed event
        """
        return HttpResponse(
            content = f"Webhook Received: {event['type']}", 
            status = 200)  