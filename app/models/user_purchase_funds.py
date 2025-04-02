from tortoise.models import Model
from tortoise import fields
from app.models.base_models import AbstractBaseModel


class UsersPurchaseFunds(AbstractBaseModel,Model):
    scheme_name = fields.CharField(max_length=150)
    scheme_code = fields.CharField(max_length=50)
    net_asset_value = fields.FloatField()             #nav value of fund at time of purchase
    latest_net_asset_value = fields.FloatField()     #nav value of fund at after hourly update 
    scheme_category = fields.CharField(max_length = 200)
    mutual_fund_family = fields.CharField(max_length = 200)
    amount = fields.FloatField()
    purchased_unit = fields.FloatField()              #calulate unit on amount basis
    current_value = fields.FloatField()
    user = fields.ForeignKeyField("models.Users", related_name="user_purchase_funds", on_delete=fields.CASCADE)
    class Meta:
        table = "user_purchase_funds"
