from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django import forms
from .managers import CustomUserManager

ROLE_CHOICES = (
    #(vale in database, display)
    ('student', 'Student'),
    ('profession', 'Professional'),
)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.pk, filename)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    file_upload = models.FileField(upload_to= user_directory_path, blank=True, null=True)



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


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)