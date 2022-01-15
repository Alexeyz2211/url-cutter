import string
import random

from django.shortcuts import render, redirect

from .forms import UrlForm
from .models import ShortUrls
from django.contrib.auth.decorators import login_required


@login_required()
def shorturl(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(6))
        urls = [u.prime_url for u in ShortUrls.objects.all()]
        url = form.cleaned_data['prime_url']
        if url not in urls:
            new_url = ShortUrls(prime_url=url, slug=slug, user=request.user)
            new_url.save()
            request.user.shorturls_set.add(new_url)
            return redirect('main:user-page')
        else:
            return redirect('main:user-page')

    else:
        form = UrlForm()
        data = ShortUrls.objects.all()
        context = {
            'form': form,
            'data': data
        }
        return render(request, 'main/index.html', context)


def redirect_on_prime_url(request, slugs):
    data = ShortUrls.objects.get(slug=slugs)
    return redirect(data.prime_url)


@login_required()
def user_detail_urls(request):
    data = ShortUrls.objects.filter(user=request.user)
    context = {
        'data': data
    }
    return render(request, 'main/user_detail_urls.html', context)
