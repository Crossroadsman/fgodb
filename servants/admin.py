from django.contrib import admin

from servants import models


# Register your models here.
models = [
    models.Servant,
    models.Rarity,
    models.Kind,
    models.Group,
    models.GpTier,
    models.Servant_X_GpTier,
    models.CommandCard,
    models.Servant_X_CommandCard,
]

for model in models:
    admin.site.register(model)
    
