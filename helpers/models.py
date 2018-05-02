from django.db import models


class BaseModel(models.Model):
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def get_model_fields(model):
        return model._meta.get_fields(include_hidden=True)
