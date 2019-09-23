from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        try:
            request.data['owner']
            return (
                request.user.id == int(request.data['owner'])
                or request.user.is_staff
            )
        except KeyError:
            return True

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'is_private') and obj.is_private is False:
            return True
        return obj.owner_id == request.user.id or request.user.is_staff


class IsOwnerOrAdminSong(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.id == view.kwargs['parent_lookup_user']
            or request.user.is_staff
        )
