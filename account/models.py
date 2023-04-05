from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    User = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="کاربری", related_name='profile')
    # Name = models.CharField(max_length=100, verbose_name="نام")
    # Family = models.CharField(max_length=100, null=True, verbose_name="نام خانوادگی")
    # Email = models.EmailField(max_length=100, verbose_name="ایمیل")

    phone = models.CharField(max_length=11, verbose_name="شماره همراه")
    profileImage = models.ImageField(upload_to="ProfileImage/", null=True, verbose_name="عکس پروفایل")
    men = 1
    women = 2
    noidea = 3
    gender_choices = [(men, 'مرد'), (women, 'زن'), (noidea, 'نظری ندارم')]
    gender = models.IntegerField(choices=gender_choices, verbose_name="جنسیت", null=True)
    bornDate = models.DateField(verbose_name="تاریخ تولد", null=True)
    credit = models.IntegerField(verbose_name="اعتبار", default=0)

    def __str__(self):
        return "نام کاربر:  {} {} ".format(self.User.first_name, self.User.last_name)