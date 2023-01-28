import puppy_state
import state_eat

class StateAsleep(puppy_state.PuppyState):
    """ Concrete StateAsleep class has a play and feed method. """
    def play(self, puppy):
        """Play method returns a string that the puppy is sleeping.
        Attributes:
            puppy (Puppy): represents a puppy
        """
        # if the user attempts to play with the puppy will reset the feeds and plays
        if puppy.plays >= 2:
            puppy.reset()
        return "The puppy is sleeping."

    def feed(self, puppy):
        """ Feed method returns a string that the puppy is now awake.
        Attributes:
            puppy (Puppy): represents a puppy
        """
        puppy.inc_feeds() # increments the number of feeds
        # resets the feeds if, feeds >= 2
        if puppy.feeds >= 2:
            puppy.reset()
        # changes the state of the puppy to state_eat
        puppy.change_state(state_eat.StateEat())
        return "The puppy is now awake, and eating."