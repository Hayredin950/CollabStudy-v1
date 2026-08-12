from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from base.models import User


class CollabStudySocialAccountAdapter(DefaultSocialAccountAdapter):
    """Maps Google/GitHub profile data onto the custom User fields.

    The User model has a custom ``name`` field and a unique ``username``;
    allauth fills standard fields (email, first/last name) automatically,
    this adapter fills the rest and guarantees a unique username.
    """

    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        provider = sociallogin.account.provider
        extra = sociallogin.account.extra_data or {}

        # Display name (Google: "name"; GitHub: "name" or the login handle)
        name = data.get('name') or extra.get('name') or ''
        if name:
            user.name = name

        # Unique username (GitHub login handle when available)
        if not user.username or User.objects.filter(username=user.username).exclude(pk=user.pk).exists():
            base = ''
            if provider == 'github':
                base = extra.get('login') or data.get('login') or ''
            base = base or (user.email or 'user').split('@')[0]
            user.username = base
            suffix = 1
            while User.objects.filter(username=user.username).exclude(pk=user.pk).exists():
                suffix += 1
                user.username = f'{base}{suffix}'

        return user
