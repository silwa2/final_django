import logging
from django.shortcuts import render
from .forms import UserForm

logger = logging.getLogger(__name__)


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']

            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {phone=}, {address=}.')
    else:
        form = UserForm()
        return render(request, 'myapp4/user_form.html', {'form': form})
