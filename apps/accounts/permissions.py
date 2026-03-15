from functools import wraps

from django.core.exceptions import PermissionDenied


def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated:
                raise PermissionDenied('Authentication required.')

            profile = getattr(user, 'profile', None)
            if profile is None or profile.role not in allowed_roles:
                raise PermissionDenied(
                    'You do not have permission to perform this action.'
                )

            return view_func(request, *args, **kwargs)

        return wrapped_view

    return decorator
