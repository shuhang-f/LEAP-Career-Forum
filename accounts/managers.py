from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, id=None, email=None, password=None, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not id and not email:
            raise ValueError(_("Either ID or email must be set"))
        if email:
            email = self.normalize_email(email)
            extra_fields.setdefault('username', email)
        user = self.model(id=id, **extra_fields)
        user.set_password(password)
        user.save()
        return user
        
    def get_by_natural_key(self, email):
        return self.get(email=email)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)