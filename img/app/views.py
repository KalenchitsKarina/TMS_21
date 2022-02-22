import requests
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from .models import NatureImage


def use_form(request):
    if request.method == "GET":
        if request.path == "/img/":
            context = {'type': 'Get'}
            template = loader.get_template('img_form.html')
            return HttpResponse(template.render(context, request))
        elif request.path == "/img/save/":
            context = {'type': 'Get'}
            template = loader.get_template('img_save.html')
            return HttpResponse(template.render(context, request))
    elif request.method == "POST":
        if request.path == "/img/":
            data = request.POST
            height = data.get("height")
            width = data.get("width")
            url = 'https://picsum.photos/' + str(width) + '/' + str(height)
            print(url)
            response = requests.get(url)
            print(response.url)
            request.session['url'] = response.url
            request.session['height'] = height
            request.session['width'] = width
            context = {'type': 'Post', 'url': response.url}
            template = loader.get_template('img_show.html')
            return HttpResponse(template.render(context, request))
        elif request.path == "/img/show/":
            data = request.POST
            comment = data.get("comment")
            url = request.session.get('url')
            height = request.session.get('height')
            width = request.session.get('width')
            image = NatureImage(url=url, height=height, width=width, comment=comment)
            try:
                image.save()
            except Exception as err:
                print(err)
                return HttpResponse(status=409)
            request.session['comment'] = comment
            return redirect('/img/save/')
        elif request.path == "/img/save/":
            print('ok')
            data = request.POST
            email = data.get("email")
            if 'url' in request.session:
                url = request.session.get('url')
            if 'comment' in request.session:
                comment = request.session.get('comment')
            context = {'url': url, 'comment': comment}
            html_message = loader.render_to_string('img.html', context)
            send_mail(
                subject='Random image from HW24',
                message='"' + str(comment) + '"',
                html_message=html_message,
                from_email='kkalenchits@yandex.by',
                recipient_list=[str(email)],
                fail_silently=False,
            )
            return redirect('/img/')









