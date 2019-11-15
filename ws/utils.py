from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections
from channels.db import database_sync_to_async
from rest_framework.authtoken.models import Token
from .exceptions import ClientError
from dispatch.models import Cop

import logging
# This decorator turns this function from a synchronous function into an async one
# we can call from our async consumers, that handles Django DBs correctly.
# For more, see http://channels.readthedocs.io/en/latest/topics/databases.html
@database_sync_to_async
def get_room_or_error(room_id, user):
    """
    Tries to fetch a room for the user, checking permissions along the way.
    """
    # Check if the user is logged in
    if not user.is_authenticated:
        raise ClientError("USER_HAS_TO_LOGIN")
    # Find the room they requested (by ID)
    try:
        room = Cop.objects.get(pk=room_id)
    except Cop.DoesNotExist:
        raise ClientError("ROOM_INVALID")
    # Check permissions
    if room.staff_only and not user.is_staff:
        raise ClientError("ROOM_ACCESS_DENIED")
    return room


@database_sync_to_async
def get_cop_or_error(socket_id):

    # Find the room they requested (by ID)
    try:
        cop = Cop.objects.get(pk=room_id)
    except Cop.DoesNotExist:
        raise ClientError("COP_INVALID")
    # Check permissions
    if cop.status == Cop.STATUS_OFFLINE:
        raise ClientError("COP_ACCESS_DENIED")
    return cop


@database_sync_to_async
def fetch_user_from_token(token_key):
    try:
        token = Token.objects.get(key=token_key)
    except Token.DoesNotExist:
        return AnonymousUser()
    return token.user
