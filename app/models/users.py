from tortoise.models import Model
from tortoise import fields
from app.models.base_models import AbstractBaseModel


class Users(AbstractBaseModel,Model):
    name = fields.CharField(max_length=50)
    email = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=150,null=True,blank=True)
    status = fields.BooleanField(default=True)

    class Meta:
        table = "users"
