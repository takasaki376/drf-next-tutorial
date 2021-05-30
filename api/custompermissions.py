from rest_framework import permissions

class OwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # GETメソッドの場合は無条件の許可する
        if request.method in permissions.SAFE_METHODS:
            return True
        #  GETメソッド以外は、 owner とログインユーザが一致する場合のみ許可する
        return obj.owner.id == request.user.id
