from hello_world.forms import MessageForm
from hello_world.models import Message
from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.
def hello_world(request):
    return render(request, 'hello_world.html', {})


def chat(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = Message(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
            )
            message.save()

    message_list = Message.objects.all().order_by('-created_on')
    paginator = Paginator(message_list, 5)  # Show 5 messages per page
    page = request.GET.get('page')
    messages = paginator.get_page(page)
    context = {
        "messages": messages,
        "form": form,
    }
    return render(request, "chat.html", context)
