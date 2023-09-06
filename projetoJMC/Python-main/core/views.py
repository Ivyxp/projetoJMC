from django.shortcuts import render, redirect
from .models import Carro

# Create your views here.
def home(request):
    carros = Carro.objects.all()
    return render(request, "index.html", {"carros": carros})
    
def salvar(request):
    tipo = request.POST.get('tipo')
    modelo = request.POST.get('modelo')
    marca = request.POST.get('marca')
    cor = request.POST.get('cor')
    preco = request.POST.get('preco')
    ano = request.POST.get('ano')
    km = request.POST.get('km')
    pagamento = request.POST.get('pagamento')
    leilao = request.POST.get('leilao') == 'true'  # Converte para valor booleano
    Carro.objects.create(tipo=tipo, modelo=modelo, marca=marca, cor=cor, preco=preco,ano=ano, km = km, pagamento=pagamento, leilao = leilao)
    carros = Carro.objects.all()
    return render(request, "index.html", {"carros": carros})


def editar(request, id):
    carro = Carro.objects.get(id=id)
    return render(request, "update.html", {"carro": carro})

def update(request, id):
    
    tipo = request.POST.get('tipo')
    modelo = request.POST.get('modelo')
    marca = request.POST.get('marca')
    cor = request.POST.get('cor')
    preco = request.POST.get('preco')
    ano = request.POST.get('ano')
    km = request.POST.get('km')
    pagamento = request.POST.get('pagamento')
    leilao = request.POST.get('leilao') == 'true' 
    
    carro = Carro.objects.get(id=id)
    #atualizando os valores
    carro.tipo = tipo
    carro.modelo = modelo
    carro.marca = marca
    carro.cor = cor
    carro.preco = preco
    carro.cor = cor
    carro.ano = ano
    carro.km = km
    carro.pagamento = pagamento
    carro.leilao = leilao
    #salvando os novs valores no banco
    carro.save()
    return redirect(home)


def delete(request, id):
    carro = Carro.objects.get(id=id)
    carro.delete()
    return redirect(home)



def mostrar(request):
    carro = Carro.objects.all()
    return render(request, 'mostrar.html', {'carros': carro})