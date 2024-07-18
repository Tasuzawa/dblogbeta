from django.shortcuts import render

# Create your views here.
def main(request):
    template_render = 'views/main/index.html'
    
    return render(request, template_render)