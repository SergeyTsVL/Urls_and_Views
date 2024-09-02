from django.shortcuts import render

# Create your views here.
def index(request):
    text = 'Это шаблон для классового представления'
    context = {
        'text': text,
    }
    return render(request, 'class_template.html', context)

def index1(request):
    text1 = 'Это шаблон для функционального представления'
    context = {
        'text1': text1,
    }
    return render(request, 'func_template.html', context)


# python manage.py runserver
# cd UrbanDjango