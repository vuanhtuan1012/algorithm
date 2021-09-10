# All You Can Eat

To attract tourists, a casino in Las Vegas proposes an all-you-can-eat buffet where guests only pay what they want to pay.

Given what each guest is ready to pay, you have to compute the restaurants gains for the day:

-   at the beginning of the day the restaurant is empty
-   a guest arrives, finds a seat, eats, pays and leaves
-   there are only  **`nb_seats`**  available. Guests can only eat and pay  **when they can be seated**
-   a guest which enters the restaurant and cannot find a seat  **waits in line until a seat is made available or until he/she gets bored and leaves**
-   a guest may come  **several times during the day**, in that case, he/she will pay at most once

Implement the method  **`computeDayGains(nb_seats, paying_guests, guest_movements)`**  which returns the gains for the day :

-   the array  **`paying_guests`**  gives what guests are ready to pay (for example if  **`paying_guests(5)`**  value is 25, it means that guest with id  **5**  is ready to pay 25 EUR for the buffet
-   the array  **`guest_movements`**  gives in order the arrivals and departures of guests. The first time you see an id, it indicates an arrival. The second time you see the same id, it indicates a departure. An arrival is always followed later in the day by a departure.

**Solution:**

- code: [all_you_can_eat.py](all_you_can_eat.py)
- test cases: [all_you_can_eat.py](../tests/all_you_can_eat.py)