class PlayingCard:
    x = 'heart', 'queen', 'king'
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        return f'{self.rank} \n{self.suit}'
    def __eq__(self, other):
        return PlayingCard.x.index(self.rank) == PlayingCard.x.index(other.suit)
    def __ne__(self, other):
        return PlayingCard.x.index(self.rank) != PlayingCard.x.index(other.suit)
    def __lt__(self, other):
        return PlayingCard.x.index(self.rank) < PlayingCard.x.index(other.suit)
    def __le__(self, other):
        return PlayingCard.x.index(self.rank) <= PlayingCard.x.index(other.suit)
    def __gt__(self, other):
        return PlayingCard.x.index(self.rank) > PlayingCard.x.index(other.suit)
    def __ge__(self, other):
        return PlayingCard.x.index(self.rank) >= PlayingCard.x.index(other.suit)


card1 = PlayingCard('king', 'heart')
card2 = PlayingCard('queen', 'heart')
card3 = PlayingCard('king', 'heart')
print(card1 > card3)

