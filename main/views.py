from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'myName' : 'Arya Kusuma Daniswara',
        'class' : 'PBP B',
        'appName' : 'inventory00',
        'name': 'Botol',
        'amount': '2',
        'description' : 'Botol 500 ml yang sangat bagus'
    }

    return render(request, "main.html", context)