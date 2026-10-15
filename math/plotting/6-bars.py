#!/usr/bin/env python3
"""Plot a stacked bar graph of fruit."""

import numpy as np
import matplotlib.pyplot as plt


def bars():
    """Display the quantity of fruit for each person."""
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    people = ['Farrah', 'Fred', 'Felicia']

    plt.bar(people, fruit[0], width=0.5, color='red',
            label='Apples')
    plt.bar(people, fruit[1], width=0.5, bottom=fruit[0],
            color='yellow', label='Bananas')
    plt.bar(people, fruit[2], width=0.5,
            bottom=fruit[0] + fruit[1],
            color='#ff8000', label='Oranges')
    plt.bar(people, fruit[3], width=0.5,
            bottom=fruit[0] + fruit[1] + fruit[2],
            color='#ffe5b4', label='Peaches')

    plt.ylabel('Quantity of Fruit')
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))
    plt.title('Number of Fruit per Person')
    plt.legend()
