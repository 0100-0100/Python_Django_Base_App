from django.shortcuts import render

from webpush import send_user_notification

def notify(request):
    payload = {
        'head': 'Hey hey hey!!',
        'body': f'Hello, {request.user}',
    }
    send_user_notification(user=request.user, payload=payload, ttl=1000)
    webpush = {'group': 'diego'}
    return render(request, 'notify.html', {'webpush': webpush})
