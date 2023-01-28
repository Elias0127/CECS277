import state_asleep

class Puppy:
    """ Puppy class represents a puppy that can play, eat, and sleep. Starts in a
    sleep state 0 # of feeds and plays. """
    def __init__(self):
        """ Initializes the puppy in a sleep state with 0 amount of feeds and plays. """
        self._state = state_asleep.StateAsleep()
        self._feeds = 0
        self._plays = 0

    @property
    def plays(self):
        """ Returns the the number of plays. """
        return self._plays

    @property
    def feeds(self):
        """ Returns the number of feeds. """
        return self._feeds

    def change_state(self, new_state):
        """ Changes the state of the puppy. Passes in the new state.
        Attributes:
            new_state (puppy_state): state of puppy
        """
        self._state = new_state

    def throw_ball(self):
        """ throw_ball returns the play method of which state the puppy is in. """
        return self._state.play(self)

    def give_food(self):
        """ give_food returns the feed method of which state the puppy is in. """
        return self._state.feed(self)

    def inc_feeds(self):
        """ Increments the # of feeds the puppy has received. """
        self._feeds += 1

    def inc_plays(self):
        """ Increments the # of plays the puppy has received. """
        self._plays += 1

    def reset(self):
        """ Resets the # of feeds and plays to 0. """
        self._feeds = 0
        self._plays = 0