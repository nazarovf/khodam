from django.shortcuts import render
import random

def generate_khodam(request):
    khodams = ['kambing congek', 'ayam kampung', 'harimoi', 'buaya darat', 'ular ijo', 'tikus bau', 'singa kalem', 'monyet rakus', 'naga item']
    khodam = None
    if request.method == 'POST':
        name = request.POST.get('inputName')
        if name:
            khodam = random.choice(khodams)
    return render(request, 'khodam_app/index.html', {'khodam': khodam})
