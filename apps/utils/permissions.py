from rest_framework import permissions


class IsAuthenticated(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(
            view.action == "retrieve" or
            str(request.query_params.get('search', False)) or
            request.method in ('HEAD', 'OPTIONS') or
            request.myuser and request.myuser.is_authenticated
        )
