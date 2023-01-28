import puppy_state
import state_play
import state_asleep

class StateEat(puppy_state.PuppyState):
    """ Concrete StateEat class has a play and feed method. """
    def play(self, puppy):
        """Play method returns a string that the puppy is either tired and sleeping or playing.
        Attributes:
            puppy (Puppy): represents a puppy
        """
        # if the user attempts to play with the puppy too much, the puppy gets tired and sleeps
        puppy.inc_plays()
        if puppy.plays >= 2:
            puppy.change_state(state_asleep.StateAsleep())
            puppy.reset()
            return "The puppy is tired of playing, the puppy is now sleeping."
        # or the puppy will begin to play
        else:
            puppy.change_state(state_play.StatePlay())
            return "The puppy is now playing."

    def feed(self, puppy):
        """ Feed method returns a string that the puppy is now full and sleeping or
        continuing to eat.
        Attributes:
            puppy (Puppy): represents a puppy
        """
        # increments the number of feeds
        puppy.inc_feeds()
        # if the puppy has been fed 2 or more time changes the puppy to a sleep state
        if puppy.feeds >= 2:
            puppy.change_state(state_asleep.StateAsleep())
            puppy.reset()
            return "The puppy is now full and sleeping."
        # otherwise returns string that the puppy continues to eat
        else:
            return "The puppy continues to eat."
