from rest_framework.permissions import BasePermission


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'is_private') and obj.is_private is False:
            return True
        return obj.users == request.user or request.user.is_staff

    def has_permission(self, request, view):
        return (
            request.user.id == view.kwargs['parent_lookup_user_playlists']
            or request.user.is_staff
        )


class IsOwnerOrAdminSong(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.id == view.kwargs['parent_lookup_user']
            or request.user.is_staff
        )
