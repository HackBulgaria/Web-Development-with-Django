from channels import Group
from channels.auth import channel_session_user_from_http, channel_session_user


@channel_session_user_from_http
def ws_add(message):
    message.reply_channel.send({"accept": True})
    Group('chat_room_{}'.format(message['path'].split('-')[-1])).add(message.reply_channel)


@channel_session_user
def ws_message(message):
    Group('chat_room_{}'.format(message['path'].split('-')[-1])).send({
        'text': "{}: {}".format(message.user, message.content['text'])
    })


@channel_session_user
def ws_disconnect(message):
    Group('chat_room_{}'.format(message['path'].split('-')[-1])).discard(message.reply_channel)
