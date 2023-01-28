import die


class Player:
    """
    Represents a list of 3 Die objects and the player’s points.

    Attributes: dice (int): sorts the list of three Die objects
                points (int): stores the player’s points/score
    """
    def __init__(self):
        self.dice = [die.Die(), die.Die(), die.Die()]
        self.points = 0

    def get_points(self):
        """
        :return: the total points
        """
        return self.points

    def roll_dice(self):
        """
        calls roll on each of the Die objects in the dice list and sorts the list.
        """
        # Iterating through the roll function from die class
        for i in self.dice:
            i.roll()
        # sorts the list
        self.dice.sort()

    def has_pair(self):
        """
        Returns true if two dice in the list have the same value.
        Increments points by 1.
        :return: boolean
        """
        if self.dice[0] == self.dice[1] or self.dice[1] == self.dice[2]:
            self.points += 1
            return True

    def has_three_of_a_kind(self):
        """
        Returns true if all three dice in the list have the same value. And increments the player points by 3.
        :return: boolean
        """
        if self.dice[0] == self.dice[1] == self.dice[2]:
            self.points += 3
            return True

    def has_series(self):
        """
        Returns true if the values of each of the dice in the list are in a sequence
        :return: boolean
        """
        if self.dice[1] - self.dice[0] == 1 and self.dice[2] - self.dice[1] == 1:
            self.points += 2
            return True

    def __str__(self):
        """
        :return: a string in the forma
        """
        return "D1=" + str(self.dice[0]) + " D2=" + str(self.dice[1]) + " D3=" + str(self.dice[2])






