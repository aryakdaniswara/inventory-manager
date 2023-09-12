from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Botol',
        'amount': '2',
        'description' : 'Botol 500ml yang sangat bagus'
    }

    return render(request, "main.html", context)