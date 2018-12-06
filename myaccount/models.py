from django.db import models
# from phone_field import PhoneField
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    #helps django work with the custom models#

    def create_user(self,email,full_name,address,phone_num,Password=None):

        #creates a new user profile object#

        if not email:
            raise ValueError('User must have a valid email address')

        email=self.normalize_email(email)
        user=self.model(email=email,full_name=full_name,address=address,phone_num=phone_num)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email,full_name,address,phone_num,password):
        if not email:
            raise ValueError("Please enter the valid email address to register yourself")
        user = self.model(email=email,
                                full_name=full_name,
                                address=address,
                                phone_num=phone_num)
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user




class UserProfile(AbstractBaseUser):
    #providing user profile custom model in the system#
    full_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150,unique=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    re_password=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone_num=models.CharField(max_length=50)
    is_doctor=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False)
    is_medistore=models.BooleanField(default=False)
    is_lab=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects= UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS =['full_name','address','phone_num']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self,app_label):
        return True


    @property
    def is_staff(self):
        "Is the user a member of staff?"# Simplest possible answer: All admins are staff
        return self.is_admin

    def get_short_name(self):
        return self.email
