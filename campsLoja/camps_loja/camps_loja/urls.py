from django.contrib import admin
from django.urls import path
from app_camps import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app_camps.views import ProdutoDetailView
from app_camps.views import carrinho, adicionar_ao_carrinho, remover_do_carrinho

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home,name='home'),
    path('produtos/', views.produtos,name='produtos'),
    path('contato/', views.contato,name='contato'),
    path('perfil/', views.perfil,name='perfil'),
    path('lookbook/', views.lookbook,name='lookbook'),
    path('login/', views.login_view,name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
     path('carrinho/', views.carrinho, name='carrinho'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

