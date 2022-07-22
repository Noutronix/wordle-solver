# wordle-solver

This program is intended to solve any given wordle answer in the least amount of guesses possible. The program functions by taking a squared average of the different outcomes that a guessed word can have (ex: all greys, one green and the rest greys, etc.) to determine which guess will eliminate, on average, the highest number of words. My program is, at the time of writing (2022-07-22), 80th out of 317 on the "wordle bot leaderboard," with an average of 3.4389 guesses needed to determine the answer of any given word. It always uses the word "SALET" to begin. 

To use this program, simply type in the guess given by the program into wordle; next, type in the results of this guess (0 for grey, 1 for yellow, 2 for green) into the "results:" prompt. For example, if the program starts with "SALET" and wordle says that "S" is green and "A" is yellow, the appropriate syntax for the prompt is "21000". 

Here is the website for wordle: https://www.nytimes.com/games/wordle/index.html
Here is the website of the wordle bot leaderboard: https://freshman.dev/wordle/#/leaderboard; my solver is named "Noutronix".
