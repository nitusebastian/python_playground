from random import randint
import pygal

class Die():
    """A class representing a single die"""

    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

die = Die()

results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')