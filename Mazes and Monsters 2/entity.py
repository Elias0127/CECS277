import abc

class Entity(abc.ABC):
    """ Represents an entity with a name and max hit points(max_hp). Initializes
     hp to the max_hp and max_hp to _max_hp.
     Attributes:
         name (str): Name of entity
         _max_hp (int): Maximum hit points
         _hp (int): Current hit points
    """
    def __init__(self, name, max_hp):
        """ Initializes attributes of entity class _name, _max_hp, _hp. """
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp

    @property
    def name(self):
        """ Name property to return the name of the entity. Accessible from any child class. """
        return self._name

    @property
    def hp(self):
        """ Hp property to return the hp of the entity. Accessible from any child class."""
        return self._hp

    def take_damage(self, dmg):
        """ Take damage applies damage to the entity it is called upon. Passes in
        damage (dmg). Subtracts the damage from the entities hit points (hp). If entities
        hp is less than zero set it equal to zero.
        Attributes:
            dmg (int): represents random damage value
            _hp (int): hit points of the applicant
        """

        self._dmg = dmg
        self._hp = self._hp - dmg
        if self._hp < 0:
            self._hp = 0

    def heal(self):
        """ Heal method restores the heroe's hp back to max_hp. """
        self._hp = self._max_hp

    @abc.abstractmethod
    def attack(self, entity):
        """ Abstract Attack method passes requires inherited classes to override.
        Passes in an entity.
        Attributes:
            entity(Entity): represents an entity with a name, hp, and location
        """
        pass

    def __str__(self):
        """ String representation of the entity. Returns Name: hp/max_hp """

        return self._name + "\nHP: " + str(self._hp) + "/" + str(self._max_hp)
