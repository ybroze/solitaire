# A Solitaire Investigation

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

I have no clue where this game came from or what its name is, but it was
apparently played in the Pacific Northwest in the mid-1900s.

This code was just to answer a question, and not written with collaboration in
mind. Apologies for any terse comments and lack of docstrings.

More [at the Stacoscimus blag](
    http://www.stacoscimus.com/a-solitaire-investigation/
).
