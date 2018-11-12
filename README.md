# A fun project for chess analysis focusing on positional play

Motivations:
- Play around with a fun project and keep my python sharp.
- Chess analysis often focuses on strategic play on a computer level: We do not expect computers to flesh out heuristic positional "lines". Computers can grind out certain positions and help flesh out concrete lines but do not help in creating theory. Is there indeed a way to analyze *positional* aspects of chess more thoroughly?

## Key Goals
- Be able to track pieces in relation to each other. Want to be able to answer the question: how frequently is the white c pawn a critical piece in the :any opening here: and how many pieces attack/guard it?.

- "Key squares": dynamically identify key squares with metrics such as "how many squares can the queen move to in the middle game". We can form heuristic metrics such as how mobile a piece is by what percentage of squares it can move to at any time. Or, perhaps give it a pass on that if it guards a key square.

- Try to see if there are strong correlations between any interesting metric that we discover and generally winning games and/or positions.

## Success Metrics
- Uncover a positional metric that definitively correlates with the fact that Magnus Carlsen is a strong player

- (Reach): Create predictive scores for matchups that perform within a reasonable amount of elo. 