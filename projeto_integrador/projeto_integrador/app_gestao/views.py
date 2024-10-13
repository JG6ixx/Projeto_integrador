from django.shortcuts import render, redirect
from .forms import UsuariosForm

def coleta_dados_usuario(request):
    if request.method == "POST":
        form = UsuariosForm(request.POST, request.FILES)  # Inclui dados e arquivos
        if form.is_valid():
            form.save()  # Salva os dados no banco
            return redirect('pagina_sucesso')  # Redireciona para a página de sucesso
    else:
        form = UsuariosForm()
    return render(request, 'cadastro.html', {'form': form})  # Passa o formulário para o template


def cadastro(request):
    return render(request, 'cadastro.html')  # Certifique-se de que 'cadastro.html' é o template correto


