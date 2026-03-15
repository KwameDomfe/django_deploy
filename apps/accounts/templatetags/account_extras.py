from django import template

register = template.Library()


@register.filter
def user_role(user):
    if not getattr(user, 'is_authenticated', False):
        return ''

    profile = getattr(user, 'profile', None)
    if profile is None:
        return 'Viewer'

    return profile.get_role_display()
