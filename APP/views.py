from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, FileResponse, JsonResponse, Http404
from random import randint
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from django.template.loader import get_template
from APP.models import Category, Products, Order
class Product:
    __max_id = 0

    def __init__(self, category: str,
                 name: str,
                 color: str,
                 price: int,
                 access: str):
        self.id = Product.__max_id
        self.category = category
        self.name = name
        self.color = color
        self.price = price
        self.access = access
        Product.__max_id += 1

    def hello(request):
        data = {'Cat, dog, parrot':'category','Scotland, haski, wavy':'name','Grey, black, green':'color','Collar, leash, stick':'access'}
        data2 = {'Category':'Кот, собака, попугай','Name':'Шотландский, хаски, волнистый',
                 'Color':'Серый, черный, зеленый','Access':'Ошейник, поводок, жердочка'}
        return JsonResponse(data)


    def __str__(self):
        return (
            f'ID: {self.id}<br>'
            +f'Категория: {self.category}<br>'
            +f'Имя: {self.name}<br>'
            +f'Цвет: {self.color}<br>'
            +f'Аксессуар: {self.access}<br>'
        )

products = [Product('Кот','Шотландский-Вислоухий','Черно-Белый','20000','Ошейник в Цветочек'),
            Product('Кот','Сфинкс','Бежевый','30000','Когтеточка'),
            Product('Собака','Хаски','Белый','40000','Поводок'),
            Product('Попугай','Волнистый','Лаймовый','1000','Колокольчик'),
            Product('Собака','Овчарка','Черный','15000','Ошейник'),
            Product('Попугай','Корелла','Серый','5000','Колечко')]

@csrf_exempt
def products_view(request: HttpResponse):
    if request.method == "GET":
        category = request.GET.get('category', None)
        print(repr(category), repr(products[-1].category))
        return HttpResponse(',\n\n'.join(str(product) for product in products
                                        if category is None
                                        or category == product.category))
    
    if request.method == 'POST':
        body = [element.strip() for element in
                request. body.decode( 'UTF-8').split('\n')]

        products.append(Product(
            category = body[0],
            name = body[1],
            color = body[2],
            price = int(body[3]),
            access = body[4]
        ))
        return HttpResponse(str(products[-1]), status=200)

    return HttpResponse(status=405)


@csrf_exempt
def product_view(request: HttpResponse, id: int):
    filtered = [product for product in products if product.id == id]

    if len(filtered) == 0:
        return HttpResponse(status=404)

    product = filtered[0]
    
    if request.method == 'GET':
        if product.name == '':
            return HttpResponseRedirect(reverse('products'))

        return HttpResponse(str(product))

    return HttpResponse(status=405)


dict = {'Cat':'D:\Programming\\Python\ПРОЕКТ\\pet_shop\\images\\vislouhie-koty-serogo-okrasa.jpg',
            'Dog':'D:\\Programming\Python\ПРОЕКТ\\pet_shop\\images\\Sibirskaya-haski.jpg',
            'Parrot':'D:\\Programming\\Python\ПРОЕКТ\\pet_shop\\images\\1.jpeg' }

def default(request):
    return FileResponse(open(dict['Parrot'], 'rb'), as_attachment=True, filename='parrot.jpeg')

def default2(request):
    return FileResponse(open(dict['Dog'], 'rb'), as_attachment=True, filename='dog.jpg')

def default3(request):
    return FileResponse(open(dict['Cat'], 'rb'), as_attachment=True, filename='cat.jpg')

def index(request):
    return render(request, 'index.html')

def products(request):
    category_id = request.GET.get('category')
    if category_id:
        try:
            category = Category.objects.get(id=category_id)
            products = Products.objects.filter(category=category)
        except Category.DoesNotExist:
            raise Http404
    else:
        products = Products.objects.all()
    categories = Category.objects.all()
    return render(request, 'shop.html', {'products': products, 'categories': categories})

def cat1(request):
    return render(request, 'cat1.html')

def cat2(request):
    return render(request, 'cat2.html')

def dog1(request):
    return render(request, 'dog1.html')

def dog2(request):
    return render(request, 'dog2.html')

def parrot1(request):
    return render(request, 'parrot1.html')

def parrot2(request):
    return render(request, 'parrot2.html')
def buy(request):
    return render(request, 'form.html')
def thanks(request):
    FIO = request.GET['FIO']
    email = request.GET['email']
    phone = request.GET['phone']
    order = Order(FIO = FIO, email = email, phone = phone)
    order.save()
    return render(request, 'thanks.html', {'phone':phone})
def friend(request):
    return render(request, 'drakon1.html')
def fish1(request):
    return render(request, 'fish1.html')
def dog3(request):
    return render(request, 'dog3.html')
def drakon2(request):
    return render(request, 'drakon2.html')
def parrot3(request):
    return render(request, 'parrot3.html')