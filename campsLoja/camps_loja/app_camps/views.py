from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, CarrinhoItem
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.views import LoginView
from .models import CustomUser
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def home(request):
    return render(request,'home.html')

def produtos(request):

    termo_pesquisa = request.GET.get('q')

    if termo_pesquisa:
        # Se houver um termo de pesquisa, filtre os produtos por nome
        lista_de_produtos = Produto.objects.filter(Q(nome__icontains=termo_pesquisa))
    else:
        lista_de_produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'lista_de_produtos': lista_de_produtos})




class ProdutoDetailView(View):
    template_name = 'produto_detail.html'  # Crie o template para mostrar os detalhes do produto

    def get(self, request, pk):
        produto = get_object_or_404(Produto, pk=pk)
        return render(request, self.template_name, {'produto': produto})
    





def carrinho(request):
    itens = CarrinhoItem.objects.all()
    total = sum(item.subtotal() for item in itens)
    return render(request, 'carrinho.html', {'carrinho_itens': itens, 'total': total})
    
def adicionar_ao_carrinho(request, produto_id):
  
     produto = get_object_or_404(Produto, id=produto_id)
     tamanho = request.POST.get('tamanho') 
     
       
     item, created = CarrinhoItem.objects.get_or_create(produto=produto, tamanho=tamanho, defaults={'quantidade': 1})
     
     if not created:
            item.quantidade += 1
            item.save()
     messages.success(request, 'Item adicionado ao carrinho !')
      
     return redirect(reverse('produto_detail', args=[produto_id]))
 

def remover_do_carrinho(request, item_id):
    item = CarrinhoItem.objects.get(id=item_id)
    if item.quantidade > 1:
        item.quantidade -= 1
        item.save()
    else:
        item.delete()
    return HttpResponseRedirect(reverse('carrinho'))      



def perfil(request):
    return render(request,'perfil.html')
def lookbook(request):
    return render(request,'lookbook.html')
def contato(request):
    return render(request,'contato.html')


def login_view(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(request, username=username, password=senha)
        
        if user is not None:
            login(request, user)
            # Redirecione para a página desejada após o login
            return render(request,'home.html')
        else:
            messages.error(request, 'Usuário ou senha inválido')
           
    
    return render(request, 'login.html')

def cadastro(request):
   

    if request.method == "POST":
        username = request.POST.get('username')
        nome = request.POST.get('name')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        senha = request.POST.get('senha')
        confirmacao_senha = request.POST.get('senha2')

        if senha != confirmacao_senha:
            messages.warning(request, 'As senhas não coincidem.')
            
        else:
            user = CustomUser.objects.filter(username=username).first()

            if user:
                messages.warning(request, 'O usuário fornecido já está em uso.')
                
            else:
                user = CustomUser.objects.create_user(username=username, email=email, celular=celular, password=senha)
                user.first_name = nome
                user.save()

                return redirect('home')  # Redirecione para a página desejada após o cadastro

    return render(request, 'cadastro.html')

 