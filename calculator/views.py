from django.shortcuts import render
from . models import TipCalculator

# Create your views here.

def index(request):
    context = {}
    if request.method == 'POST':
        try:
            bill = float(request.POST.get('bill'))
            tip = int(request.POST.get('tip'))
            people = int(request.POST.get('people'))

            # calculate total and per person
            total_bill = bill + (bill * tip / 100)
            each = round(total_bill / people, 2)

            TipCalculator.objects.create(
                user = request.user if request.user.is_authenticated else None,
                bill = bill,
                tip_percentage = tip,
                people=people,
                total_bill=total_bill,
                per_person=each,
            )
            context['each'] = each
            context['total_bill'] = round(total_bill, 2)
        except (ValueError, TypeError):
            context['error'] = "Please enter valid numbers."
    return render(request, 'calculator/index.html', context)


