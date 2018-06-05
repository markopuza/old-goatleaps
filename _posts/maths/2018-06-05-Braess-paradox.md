---
layout: post
title:  "The Braess's paradox"
date:   2018-06-05 01:36:59 +0000
category-string: "Maths"
categories: maths
icon: braessparadox
---

The Braess's paradox was a distinctive topic when I was studying game theory, as I clearly remember how it made me go **"What?!"**. The highly unintuitive idea behind the paradox can be well demonstrated within traffic:

> In a traffic network, it is possible to **increase** the average journey time by **building** new fast fancy roads. Similarly, it is possible to **speed up** the traffic by **closing** some important roads.

For some real-world examples of the phenomenon see the >>[Boston's Big Dig](https://en.wikipedia.org/wiki/Big_Dig)<< or the >>[Closure of the 42nd Street in NYC](https://www.nytimes.com/1990/12/25/health/what-if-they-closed-42d-street-and-nobody-noticed.html)<<. Let me explain how this is possible on a toy example.

To analyse the paradox, we first need to introduce the core game theoretic concept.
**Nash equilibrium** is a measure of stability: when a game is in Nash equilibrium, no player can get better off by changing his strategy (assuming the strategies of others would remain unchanged), thus nobody really changes their strategy. We note in passing that the Nash equilibria are not unique. When perceiving a traffic network as a game where drivers are players, the Nash equilibrium will occur (quite realistically) precisely when each driver thinks something along the lines:
*"Hmmm, see all that terrible traffic that is going on today. If I try to use any other roads to get to my destination, I will surely only get slowed down. Duh".*

The Braess's paradox is actually not a paradox in the right sense, rather perhaps an absurdly-sounding demonstration of the fact that Nash Equilibria need not be optimal. Indeed, when in Nash Equilibrium, even though no player can be better off just by changing their own strategy, it is still possible that everyone could be better off if they were to change the strategies simultaneously (>>[The Prisoner's dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)<<).

For illustrative purposes, consider the following toy example. There are two routes that can get you from city A to city B, separated by a river, each consisting of two parts: one part a narrow single-track road and the other part a wide multi-lane road. There are, at one time, in average 300 drivers trying to travel between A and B. We can approximate the expected travel time on the poor single-track road as $$T/50$$ minutes, where $$T$$ is the amount of cars that choose to take it. The travel time on the wide multi-lane road, however, remains constant 11 minutes, as this road is wide enough to handle any amount of traffic. The government in attempt to speed up the travel plans to create a super fast highway-bridge in between these two roads, creating a 3 minute connection.

<div align="center">
<img src="/assets/image/braess_without.png" width="40%">
<img src="/assets/image/braess_with.png" width="40%">
</div>

But, ooh wee, what happens when the bridge is built?

1. In the scenario without bridge, every driver just wants to take the route with smaller amount of drivers. This results in a Nash Equilibrium where 150 drivers travel via the north route and 150 drivers travel via the south route. No one can improve their travel time by switching to the other route. The travel will take $$150/50 + 11 = 14$$ minutes for everyone.

2. After the bridge is built, everyone would fancy to travel via the new hyperfast bridge. One can notice that everyone travelling via the two single-track roads is now indeed a Nash Equilibrium. No one can be better off by switching their route - incorporating one multi-lane road in the travel will just increase the travel time by $$2$$ minutes, and travelling via both multi-lane roads is even worse. The travel will thus take $$300/50 + 3 + 300/50 = 15$$ minutes for everyone.

The actual travel time increases from 14 minutes to 15 minutes. Everyone wanting to travel via the bridge spoils the benefits for everyone. Note that the difference may actually be much greater than 1 minute. On the bright side, it is also bounded above - we provably cannot worsen the situation by more than a factor fo $$4/3$$, at least not in the case when the traffic times of the roads are linear functions of traffic (>>[Price of Anarchy](https://en.wikipedia.org/wiki/Price_of_anarchy)<<).

Of course the above model makes some unrealistic assumptions: the drivers behave rationally, the travel time on the single-track road is a linear function of traffic, drivers have access to the current situation in the whole network... But in any case, it illustrates that in traffic networks, as well as elsewhere, the quality can be substantially more important than quantity, and that the traffic engineering can be a much harder job than one might expect.

Did you also know that it may be a reasonable decision for the coach *not* to let the most skilled star-player into the game?
