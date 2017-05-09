from django.views.generic import ListView, CreateView, DetailView
from django.core.urlresolvers import reverse

from .models import ChatRoom


class ListChatRoomsView(ListView):
    model = ChatRoom
    template_name = 'chat/list_chat_rooms.html'


class CreateChatRoomView(CreateView):
    model = ChatRoom
    template_name = 'chat/create_chat_room.html'
    fields = ('name', 'capacity', )

    def get_success_url(self):
        return reverse('chat:list')


class DetailChatRoomView(DetailView):
    model = ChatRoom
    template_name = 'chat/chat_room.html'
    pk_url_kwarg = 'chat_room_id'
