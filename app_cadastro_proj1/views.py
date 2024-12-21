from django.shortcuts import render
from .models import Usuario


def home(request):

    return render(request,'usuarios/home.html')

def usuarios(request):

    #Salvar os dados da tela no banco de dados
    # Apenas salva o usuário se for uma requisição POST

    if request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        # Verifique se os campos foram enviados
        if nome and idade:
            novo_usuario = Usuario(nome=nome, idade=idade)
            novo_usuario.save()

    # Exibir todos os usuários já cadastrados em uma nova página

    usuarios = {

        'usuarios' : Usuario.objects.all()
    }

    #Retornar os dados para a página de lisagem de usuários

    return render(request,'usuarios/usuarios.html', usuarios)

