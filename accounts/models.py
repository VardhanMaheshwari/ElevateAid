from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password, check_password

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    USER_TYPES = [('beneficiary', 'Beneficiary'), ('donor', 'Donor')]
    SUB_TYPES = [('ngo', 'NGO'), ('college', 'College'), ('company', 'Company'), ('personal', 'Personal')]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    last_login = models.DateTimeField(null=True, blank=True, auto_now=True)
    user_type = models.CharField(max_length=12, choices=USER_TYPES)
    sub_type = models.CharField(max_length=12, choices=SUB_TYPES)

    ngo_college_company_id = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    aadhar_number = models.CharField(max_length=12, blank=True, null=True)

    password = models.CharField(max_length=255)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "phone", "address"]

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.name} - {self.user_type} ({self.sub_type})"
