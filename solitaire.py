"""
Determine the probability of winning for a particular type of solitaire game.
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
