import pygame
from settings import *
from game_stats import *

settings = Settings()
stats = GameStats(settings)


# working
def get_high_scores():
    path = settings.high_score_file
    scores = []
    file = open(path, 'r')

    list = file.readlines()
    for i in range(len(list)):
        data = list[i].split(' ')
        data[1].rstrip()
        scores.append(data)

    file.close()
    return scores


def check_high_score(self):
    score_list = self.get_high_scores()
    insert_index = -1
    player_initials = 'TST'

    for i in range(len(score_list)):
        if self.stats.high_score > int(score_list[1][0]):
            insert_index = i

    add_needed = insert_index > -1
    if add_needed:
        score_list.insert(insert_index, [self.stats.high_score, player_initials])
        self.rewrite_score_file(score_list)


def rewrite_score_file(self, score_list):
    path = self.settings.high_score_file
    file = open(path, 'w')
    lines = []

    for i in range(len(score_list)):
        lines.append(score_list[0] + " " + score_list[1])

    file.writelines(lines)

    file.close()