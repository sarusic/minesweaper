from os import replace
import numpy as np
from matplotlib import pyplot as plt

game_config = {
        "EASY": {"field_size": 9, "number_mines": 10},
        "MEDIUM": {"field_size": 16, "number_mines": 40},
        "HARD": {"field_size": 22, "number_mines": 99}
        }

def main():
    field_size, number_mines = game_config["HARD"].values()
    ones = np.ones(number_mines)
    zeros = np.zeros(field_size*field_size-number_mines)
    pool = np.concatenate((zeros, ones))
    field = np.random.choice(a=pool,size=(field_size, field_size),replace=False)
    count = np.unique(field, return_counts=True)
    print(count)

if __name__ == "__main__":
    main()
