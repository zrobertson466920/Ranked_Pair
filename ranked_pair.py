import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
from random import shuffle


def create_ranks(num_options):

    return np.zeros((num_options,num_options))


def rank_option(option,rank,i,j, notes = []):

    if np.random.randint(0,1,1) == 1:
        choice = input(option[i] + " or " + option[j] + "? (a/f)\n")
        if choice == 'a':
            rank[i][j] += 1
        elif choice == 'f':
            rank[j][i] += 1
        elif choice == '':
            rank[j][i] += 0
        else:
            notes.append(choice)
    else:
        choice = input(option[j] + " or " + option[i] + "? (a/f)\n")
        if choice == 'a':
            rank[j][i] += 1
        elif choice == 'f':
            rank[i][j] += 1
        elif choice == '':
            rank[i][j] = 0
        else:
            notes.append(choice)

    return rank, notes


def output_ranks(option,rank):

    marginal_rank = 1/(np.size(rank,axis = 1)-1) * np.sum(rank,axis = 1)
    data = list(zip(option,marginal_rank))
    data.sort(key=itemgetter(1),reverse = True)
    print(data)


if __name__ == '__main__':

    option = []
    i = 0
    action = i
    while action != 'q':
        action = input("Enter Option " + str(i+1) + " name ( or q to finish) \n")
        if action == 'q':
            continue
        else:
            option.append(action)
        i += 1
    num_options = len(option)
    num_ranks = int(num_options * (num_options - 1) / 2)

    print("Thanks! Assuming ~8s evaluation time, it'll take you " + str(8*num_ranks/60) + " minutes to finish. \n")

    rank = create_ranks(num_options)

    index = []
    for i in range(num_options):
        for j in range(i+1,num_options):
            index.append((i,j))
    shuffle(index)

    notes = []
    for i in range(num_ranks):
        if i % 10 == 0:
            print(str(i+1) + " out of " + str(num_ranks))
        rank, notes = rank_option(option,rank,index[i][0],index[i][1],notes)

    output_ranks(option,rank)
    print(notes)