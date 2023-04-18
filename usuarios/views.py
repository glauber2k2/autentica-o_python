# bibliotecas instaladas nesse projeto.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required


def cadastro(request):  # código de cadastro.
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        # verificar se ja existe um usuário igual foi enviado (com o filter).
        # o first pega o primeiro objeto achado no filtro, e caso não ache retorna "none".
        user = User.objects.filter(username=username).first()

        if user:  # verifica se foi retornado um usuario anteriormente.
            # se sim, não cadastra novamente.
            return HttpResponse("Ja existe um usuário com esse username")

        user = User.objects.create_user(
            # caso não, cadastra o novo usuario enviado.
            username=username,
            email=email,
            password=senha,
        )
        user.save()

        return HttpResponse("usuario cadastrado com sucesso")


def login(request):  # código de login.
    if request.method == "GET":  # se o método for get,
        # é apenas retornado a pagina de login.
        return render(request, "login.html")
    else:  # se for POST.
        # guarda a requisição nessas variáveis,
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        # usa o authenticate, para verificar se existe esse login cadastrado.
        # e guarda o resultado na variável user.
        user = authenticate(username=username, password=senha)

        if user:  # verifica se foi encontrado usuario ou não.
            # se sim. efetua o login, utilizando o request com a sessão, e o usuario logado.
            login_django(request, user)
            # caso seja efetuado o login.
            return HttpResponse("usuario autenticado")
        else:
            # caso não seja efetuado o login.
            HttpResponse("usuario não cadastrado")


@login_required(  # utiliza o login required para verificar se o usuario está com a sessão logada.
    login_url="/auth/login/"  # login url = para onde o usuario será redirecionado caso não esteja logado.
)
def plataforma(request):  # caso esteja, entra na pagina plataforma
    # mensagem exibida ao entrar em plataforma.
    return HttpResponse("plataforma")
