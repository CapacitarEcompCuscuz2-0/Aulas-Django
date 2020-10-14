from django.shortcuts import render

# Create your views here.

def index(request, numero):
    context = {
        'mensagem':'Blog recém-criado',
        'confirmacao': request.user.is_authenticated,
        'numero':numero,
    }
    return render(request, 'core/index.html', context)
