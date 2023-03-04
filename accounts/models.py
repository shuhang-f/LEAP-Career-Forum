from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django import forms
from .managers import CustomUserManager

ROLE_CHOICES = (
    ('student', 'Student'),
    ('profession', 'Professional'),
)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = forms.ChoiceField(choices=ROLE_CHOICES)



    groups = models.ManyToManyField(Group, related_name='customuser_groups', blank=True)
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_user_permissions',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email