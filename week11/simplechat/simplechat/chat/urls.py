from django.conf.urls import url, include

from .views import ListChatRoomsView, CreateChatRoomView, DetailChatRoomView


chat_room_patterns = [
    url(
        regex=r'^create/$',
        view=CreateChatRoomView.as_view(),
        name='create'
    ),
    url(
        regex=r'^(?P<chat_room_id>[0-9]+)/$',
        view=DetailChatRoomView.as_view(),
        name='detail'
    ),
]


urlpatterns = [
    url(
        regex=r'^$',
        view=ListChatRoomsView.as_view(),
        name='list'
    ),
    url(
        regex=r'^chat-room/',
        view=include(
            arg=chat_room_patterns,
            namespace='chat-room'
        )
    ),
]
