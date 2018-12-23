from django.db import models


class Servant(models.Model):

    fgo_id = models.IntegerField()
    name = models.CharField(max_length=255)
    rarity = models.ForeignKey(
        'Rarity',
        on_delete=models.CASCADE
    )
    kind = models.ForeignKey(
        'Kind',
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        'Group',
        on_delete=models.CASCADE
    )

    base_attack = models.IntegerField()
    max_attack = models.IntegerField()
    base_hp = models.IntegerField()
    max_attack = models.IntegerField()


class RarityManager(models.Manager):
    RARITY_MAP = {
        '1': {'cost': 3, 'max_level': 60},
        '2': {'cost': 4, 'max_level': 65},
        '3': {'cost': 7, 'max_level': 70},
        '4': {'cost': 12, 'max_level': 80},
        '5': {'cost': 16, 'max_level': 90},
    }

    def create_rarity(self, name, rating):

        rarity = self.create(
            name=name,
            rating=int(rating),
            cost=self.RARITY_MAP[rating]['cost'],
            max_level=self.RARITY_MAP[rating]['max_level']
        )

        # if desired, we can do something with the rarity object

        return rarity


class Rarity(models.Model):

    name = models.CharField(max_length=255)
    rating = models.IntegerField()
    cost = models.IntegerField()
    max_level = models.IntegerField()

    objects = RarityManager()


class Kind(models.Model):
    """`Class` in FGO parlance (but a builtin keyword in python)"""
    
    name = models.CharField(max_length=255)


class Group(models.Model):
    """`Attribute` in FGO parlance (but has a different implied meaning in
    Python.
    """
    name = models.CharField(max_length=255)


class GpTier(models.Model):
    """The servant's `tier` value as determined by grandorder.gamepress.gg
    """
    rating = models.IntegerField()
    description = models.TextField()


class Servant_X_GpTier(models.Model):
    """The MTM through table for Servant and GpTier"""
    servant = models.ForeignKey(
        'Servant',
        on_delete=models.CASCADE
    )
    gp_tier = models.ForeignKey(
        'GpTier',
        on_delete=models.CASCADE
    )

