from tortoise import Model, fields


class DateTimeMixin:
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)


class AbstractBaseModel(Model,DateTimeMixin):
    id = fields.IntField(primary_key=True)

    class Meta:
        abstract = True
