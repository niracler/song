from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return request.myuser and obj.username == request.myuser.username


class IsAuthenticatedOrSearchOnly(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(
            view.action == "retrieve" or
            request.query_params.get('search', False) or
            request.method in ('HEAD', 'OPTIONS') or
            request.myuser and request.myuser.is_authenticated
        )


class IsAuthenticatedOrSearchAndTagsOnly(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(
            view.action == "retrieve" or
            request.query_params.get('tags', False) or
            request.query_params.get('search', False) or
            request.method in ('HEAD', 'OPTIONS') or
            request.myuser and request.myuser.is_authenticated
        )
