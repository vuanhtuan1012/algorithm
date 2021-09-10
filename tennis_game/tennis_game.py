# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2021-09-10 20:48:08
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-09-10 21:10:37

def translateScore(score):
    point = 0
    if score == 1:
        point = 15
    elif score == 2:
        point = 30
    elif score == 3:
        point = 40
    return str(point)


def score(nameP1, nameP2, wins):
    score1 = sum([1 for name in wins if name == nameP1])
    score2 = sum([1 for name in wins if name == nameP2])

    res = nameP1 + ' ' + translateScore(score1) + ' - ' \
        + nameP2 + ' ' + translateScore(score2)
    diff = score1 - score2
    # duece
    if (score1 == score2) and (score2 >= 3):
        res = 'DEUCE'
    # advance
    if (diff == 1) and (score1 >= 4):
        res = nameP1 + ' Advance'
    if (diff == -1) and (score2 >= 4):
        res = nameP2 + ' Advance'
    # win
    if (diff >= 2) and (score1 >= 4):
        res = nameP1 + ' Wins'
    if (diff <= -2) and (score2 >= 4):
        res = nameP2 + ' Wins'
    return res


def main():
    nameP1 = 'P1'
    nameP2 = 'P2'
    wins = ['P1']  # P1 15 - P2 0
    print(score(nameP1, nameP2, wins))
    wins = ['P1', 'P1']  # P1 30 - P2 0
    print(score(nameP1, nameP2, wins))
    wins = ['P1', 'P1', 'P1']  # P1 40 - P2 0
    print(score(nameP1, nameP2, wins))
    wins = ['P1', 'P1', 'P1', 'P2', 'P2', 'P2']  # DUCE
    print(score(nameP1, nameP2, wins))


if __name__ == '__main__':
    main()
