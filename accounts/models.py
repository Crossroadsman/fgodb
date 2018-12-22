from django.db import models
from django.contrib.auth.models import AbstractUser


class FgoUser(AbstractUser):
    """The standard User model for the FGODB app.

    The Django docs recommend starting with a custom user model even when
    you don't expect to need any custom features, since the pain of
    migrating from the default user model later is so enormous.

    When we might reference `User` directly in the project, we instead use
    django.contrib.auth.get_user_model() which returns the currently active
    user model (custom if specified, built-in User otherwise).

    When defining relations in models, specify the custom User model using
    settings.AUTH_USER_MODEL.
    See: https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#referencing-the-user-model
    """
    pass

# Create your models here.
