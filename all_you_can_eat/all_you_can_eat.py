# -*- coding: utf-8 -*-
# @Author: anh-tuan.vu
# @Date:   2021-09-10 19:09:55
# @Last Modified by:   anh-tuan.vu
# @Last Modified time: 2021-09-10 20:05:15

# Casino All You Can Eat challenge
# https://github.com/frferrari/CasinoAllYouCanEat

def computeDayGains(nb_seats, paying_guests, guest_movements):
    restaurant = set()
    visitors = set()
    waiting = []
    for guest in guest_movements:
        if guest not in restaurant:  # arrival
            if nb_seats > 0:  # seat available
                restaurant.add(guest)
                nb_seats -= 1
                visitors.add(guest)
            else:  # seat unavailable
                if guest not in waiting:  # guest goes in waiting list
                    waiting.append(guest)
                else:  # guest gets bored and leaves
                    waiting.remove(guest)
        else:  # leave after eating
            restaurant.remove(guest)
            nb_seats += 1
            if waiting:  # exist guest(s) in waiting list
                waiting_guest = waiting.pop(0)
                restaurant.add(waiting_guest)
                nb_seats -= 1
                visitors.add(waiting_guest)
    gain = sum([paying_guests[i] for i in visitors])
    return gain


def main():
    nb_seats = 2
    paying_guests = [10, 25, 12, 42]
    guest_movements = [2, 3, 1, 0, 3, 0, 1, 2]
    gain = computeDayGains(nb_seats, paying_guests, guest_movements)
    print(gain)


if __name__ == '__main__':
    main()
