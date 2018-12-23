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
    max_hp = models.IntegerField()

    def __str__(self):
        return f'{self.name} ({self.kind})'


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

    def __str__(self):
        stars = "*" * self.rating
        return stars

    class Meta:
        verbose_name_plural = 'Rarities'  # used by django admin


class Kind(models.Model):
    """`Class` in FGO parlance (but a builtin keyword in python)"""
    
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Group(models.Model):
    """`Attribute` in FGO parlance (but has a different implied meaning in
    Python.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class GpTier(models.Model):
    """The servant's `tier` value as determined by grandorder.gamepress.gg
    """
    rating = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return str(self.rating)


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

    def __str__(self):
        return f'{self.servant} X {self.gp_tier}'


class CommandCard(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Servant_X_CommandCard(models.Model):
    """The MTM through table for Servant and CommandCard"""
    servant = models.ForeignKey(
        'Servant',
        on_delete=models.CASCADE
    )
    command_card = models.ForeignKey(
        'CommandCard',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.servant} X {self.command_card}'

