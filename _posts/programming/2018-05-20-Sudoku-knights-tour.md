---
layout: post
title:  "Finding a Sudoku knight's tour"
date:   2018-05-27 01:38:59 +0000
category-string: "Programming"
categories: programming
icon: dailyprogrammer361
---

This post will about a fun challenge of the r/dailyprogrammer subreddit. For those of you that don't know about >>[r/dailyprogrammer](https://www.reddit.com/r/dailyprogrammer/)<<, go check it out! The community of this subreddit is exceptionally friendly, and provides interesting challenges for programmers of all levels, on a regular basis.

<img src="/assets/image/knighttour.png" style="width: 25%; display: block; margin-left: auto; margin-right: auto;">

Surely everyone knows the >>[Sudoku puzzle](https://en.wikipedia.org/wiki/Sudoku)<< from the evening newspapers or elsewhere. The second ingredient of the challenge is knowing about >>[Knight's tours](https://en.wikipedia.org/wiki/Knight%27s_tour)<< (Talking about the chess knight). A Knight's tour is a sequence of consecutive knight moves, such that the knight visits each position on the $$m \times n$$ board exactly once. Such Knight's tours provably exist if certain conditions on $$m, n$$ are met, and the Sudoku's $$9 \times 9$$ board indeed meets them.

The author of the >>[dailyprogrammer's challenge #361](https://www.reddit.com/r/dailyprogrammer/comments/8ked11/20180518_challenge_361_hard_sudoku_knights_tour/)<< playfully combined the games of chess and Sudoku in the following challenge:

> Among all valid (filled-in) Sudokus $$S$$ and all valid Knight's tours $$K$$, define the scoring function: \\
  $$\ \ \ \ score(S, K) = x \in \mathbb N$$ \\
where $$x$$ is the 81-digit number whose $$i$$-th digit is the number written on the Sudoku square that the Knight visited after the $$i$$-th move in his tour. \\
Find $$S, K$$ that makes $$score(S, K)$$ as high possible.

Over the course of a week, multiple competitors were improving on the best score found thus far in a communal effort (and sharing the score). No one however managed to find a provably optimal score, so the efforts went more into (At least, I was under this impression) writing programs that, given some score, would find **a** better score. I wrote exactly this kind of program, and with a nontrivial amount of sheer luck, I managed to be the last one to improve a score. This earned me my first gold medal flair and concluded an unexpectedly fun experience!

There are still unfinished ties and ends in the challenge. **Can you find the optimal solution?** If you can, or have any other thoughts, don't hesitate to >>[contribute](https://www.reddit.com/r/dailyprogrammer/comments/8ked11/20180518_challenge_361_hard_sudoku_knights_tour/)<<.


$$$$

My program for the challenge is below:

> [dailyprogrammer361.py](/assets/code/dailyprogrammer361.py)
