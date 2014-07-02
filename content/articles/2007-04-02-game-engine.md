Title: Cross-platform Game Engine
Date: 2007-04-02 00:50:00
Author: Sean Azlin
Category: RIT
Tags: Game Development
Slug: cross-plat-game-engine

For my second CG 2 project at RIT, I proposed to design and build a simple cross-platform game engine in C++. I did it mostly on Linux using VIM and CLI tools, which was of course a blast. The engine included an adapter layer that essentially abstracted away the graphics API for a given platform when implementing the game.

{% img ../images/game_eng1.jpg 640 auto [Game Eng Screen 1] %}
{% img ../images/game_eng2.jpg 320 auto [Game Eng Screen 2] %}{% img images/game_eng3.jpg 320 auto [Game Eng Screen 3] %}
{% img ../images/game_eng4.jpg 320 auto [Game Eng Screen 4] %}{% img images/game_eng5.jpg 320 auto [Game Eng Screen 5] %}

Through this project, I succeeded in exploring the challenges of creating even the simplest game engine. As one might expect, it was a feat far more challenging than I had at first imagined. Despite this, I successfully created a POC prototype using the engine that built and ran on Linux, Unix, and Windows. It's a game that the computer plays against itself over and over in an endless battle for spherical domination.

Fun fact: The game is simple and 100% deterministic and *should* always end in a tie, but through the magic of [Chaos Theory][] it always presents the user with a vivid and unpredictable battle of cloud-like patterns.

[Chaos Theory]: http://en.wikipedia.org/wiki/Chaos_theory
