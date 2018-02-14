"""
A Solitaire Investigation
At a recent family gathering, my father showed me a solitaire game that his
father used to play. Its rules are simple:

* The goal is to discard all cards.
* Play one card at a time from the top of the deck, forming a single row of
  cards. Always play the next card to the right of the one preceding it.
* You can remove three cards at a time in any combination from the ends of the
  row (3 from one side or 2 from one and one from the other).
* The removed cards must add up to either 10, 20, or 30, with face cards
  counting as 10 and aces as 1.
* The final discard may be four cards, which are guaranteed to add up to a
  multiple of 10.

I wondered whether or not there could be a strategy to this game, or if the
outcome is strictly determined by the lay of the cards after dealing them.
That is, are there some unwinnable shuffles? And can one's strategy affect the
odds of winning given a certain shuffle?

This code is for me, not written with collaboration in mind. Apologies for any
terse comments and lack of docstrings.

More: http://www.stacoscimus.com/a-solitaire-investigation/
"""
from random import shuffle


def simulate_game():
    """Simulate a new solitaire game."""
    # Four suits with numbers 1 through 10, plus face cards.
    cards = (range(1, 11) + [10] * 3) * 4
    shuffle(cards)

    in_play = []
    for card in cards:
        # Add a new card.
        in_play.append(card)

        while True:
            # Remove cards until it is impossible.
            previous = in_play
            in_play = remove_cards(in_play)

            if previous == in_play:
                break

    return in_play


def remove_cards(in_play):
    """Remove cards from an ordered list of denominations currently in play,
    and return the remaining cards after one removal.
    """
    remaining = in_play[:]

    # Cannot remove if length is less than three.
    if len(in_play) >= 3:

        # Three from the end.
        if sum(in_play[-3:]) % 10 == 0:
            remaining = in_play[:-3]

        # 2 from the end; 1 from the start.
        elif (in_play[0] + sum(in_play[-2:])) % 10 == 0:
            remaining = in_play[1:-2]

        # 1 from the end; 2 from the start.
        elif (sum(in_play[:2]) + in_play[-1]) % 10 == 0:
            remaining = in_play[2:-1]

        # All three from the start.
        elif sum(in_play[:3]) % 10 == 0:
            remaining = in_play[3:]

    return remaining


def find_success_prob(n=10000):
    """Find the success probability given a certain number of simulated games.
    """
    wins = 0.0
    for _ in range(n):
        remaining = simulate_game()

        # A victory if we have either one or four cards adding
        # to a multiple of ten.
        if len(remaining) <= 4 and sum(remaining) % 10 == 0:
            wins += 1

    return wins / n


if __name__ == '__main__':
    print find_success_prob()
