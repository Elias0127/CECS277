import puppy_state
import state_asleep

class StatePlay(puppy_state.PuppyState):
    """ Concrete StatePlay class has a play and feed method. """
    def play(self, puppy):
        """Play method returns a string that the puppy is tired of playing and is now sleeping
        or the puppy continues to play.
        Attributes:
            puppy (Puppy): represents a puppy
        """
        # if the user attempts to play with the puppy 2 or more times
        puppy.inc_plays() # increments the # of plays
        if puppy.plays >= 2:
            puppy.change_state(state_asleep.StateAsleep()) # changes the puppy to sleep state
            puppy.reset() # resets the # of plays and feeds
            return "The puppy is tired of playing and is now asleep."
        else:
            return "The puppy continues to play."

    def feed(self, puppy):
        """ Feed method returns a string that the puppy is playing. The puppy doesn't eat
        when it's playing.
        Attributes:
            puppy (Puppy): represents a puppy
        """
        # if the puppy has attempted to been fed 2 or more times
        if puppy.feeds >= 2:
            puppy.reset() # resets the # of feeds and plays
        return "The puppy is playing."