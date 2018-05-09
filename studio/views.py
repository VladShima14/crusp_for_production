from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectImage
from .form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.


def index(request):
    projects = Project.objects.all()

    return render(request, "studio/main_page.html", context={'projects': projects})


def portfolio(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project_images = ProjectImage.objects.filter(project=project)
    project_slider = Project.objects.all()

    return render(request, 'studio/portfolio.html', context={
        "project": project,
        "project_images": project_images,
        "project_slider": project_slider,
    })


def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            email_message_form = "{},\n , {},\n, {}\n".format(message, email, name)

            recepients = ['cruspstudio@gmail.com']

            try:
                send_mail(name, email_message_form, 'cruspstudio@gmail.com', recepients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')

            return HttpResponse(request.META.get('HTTP_REFERER'))

        else:
            form = ContactForm()
