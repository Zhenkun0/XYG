from datetime import datetime

from django.core.mail import send_mail, EmailMultiAlternatives
from django.db import models
from django.template.loader import get_template
from fitness import settings
from django.contrib.auth.models import AbstractUser
from PIL import Image

from django.conf import settings


# class Trainer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     trainer = models.BooleanField("trainer", default=True)
#     image = models.ImageField(
#         null=True, upload_to="profile_pics"
#     )
#
#     def __str__(self):
#         return f"{self.user.username} Profile"
#
#     class TrainingStyle(models.TextChoices):
#         POWERLIFTING = 'powerlifting'
#         BODYBUILDING = 'bodybuilding'
#         OLYMPICLIFTING = 'olympiclifting'
#         YOGA = 'yoga'
#         PILATES = 'pilates'
#         BODYWEIGHT = 'bodyweight'
#
#     training_style = models.CharField(
#         max_length=25,
#         choices=TrainingStyle.choices,
#         default=TrainingStyle.POWERLIFTING,
#     )
#
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         # mail system
#         try:
#             email = self.user.email
#             print("\n\n\n", email, settings.EMAIL_HOST_USER)
#             email_html = get_template("email.html")
#             d = {"username": self.user.username}
#             subject = "welcome to Fitness App you are approved by Admin"
#             from_email = settings.EMAIL_HOST_USER
#             to = email
#             html_content = email_html.render(d)
#             msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
#             msg.attach_alternative(html_content, "text/html")
#             msg.send()
#         except:
#             print("email not working")
#
#         img = Image.open(self.image.path)
#         print("\n\n\n  -->  try saving image")
#         width, height = img.size
#         if height >= 300 or width >= 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)
#
#     class Meta:
#         db_table = "trainer"


class Trainee(AbstractUser):
    trainee = models.BooleanField("trainee", default=True)
    # TODO create Order class
    # trainer = models.ForeignKey(
    #     Trainer, blank=True, null=True, on_delete=models.SET_NULL
    # )
    height = models.DecimalField(max_digits=100, decimal_places=1, null=True, blank=True)
    weight = models.DecimalField(max_digits=100, decimal_places=1, null=True, blank=True)
    goal_setting = models.CharField(max_length=50, default='PowerLifting')
    dob = models.DateField(default=datetime.now)
    gender = models.CharField(max_length=6, default="Male")

    def __str__(self):
        return f"{self.username} Profile"

    class Meta:
        db_table = "trainee"
