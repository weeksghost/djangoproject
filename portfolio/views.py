from django.shortcuts import render, get_list_or_404

from portfolio.models import Work


def portfolio_list(request):
    template = 'portfolio_list.html'
    work = get_list_or_404(Work.objects.order_by('-created').filter(published=True))

    context = {
        'work': work
    }
    return render(request, template, context)
