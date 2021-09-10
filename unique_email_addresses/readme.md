# Unique Email Addresses

<!-- ## Problem -->

Every email consists of a local name and a domain name, separated by the @ sign.

For example, in  `alice@leetcode.com`, `alice`  is the local name, and  `leetcode.com`  is the domain name.

Besides lowercase letters, these emails may contain  `'.'`s or  `'+'`s.

If you add periods (`'.'`) between some characters in the  **local name**  part of an email address, mail sent there will be forwarded to the same address without dots in the local name. For example,  `"alice.z@leetcode.com"`  and  `"alicez@leetcode.com"`  forward to the same email address. (Note that this rule does not apply for domain names.)

If you add a plus (`'+'`) in the  **local name**, everything after the first plus sign will be **ignored**. This allows certain emails to be filtered, for example `m.y+name@email.com` will be forwarded to `my@email.com`. (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of  `emails`, we send one email to each address in the list. How many different addresses actually receive mails?

**Example 1:**

**Input:** ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

**Output:** 2

**Explanation:** "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails

**Note:**

-   `1 <= emails[i].length <= 100`
-   `1 <= emails.length <= 100`
-   Each  `emails[i]`  contains exactly one  `'@'`  character.
-   All local and domain names are non-empty.
-   Local names do not start with a  `'+'`  character.

(Source: [LeetCode](https://leetcode.com) - [Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/))

<!--
## Analysis

### Algorithm

For each email address we need to covert it to the _canonical_ address that actually receives the mail. The steps are:
1. remove the first `'+'` character and all characters after it in the **local name** if they exists.
2. remove all periods `'.'` in the **local name** if they exists.
3. *canonical* address = **new local name** + `'@'` + **domain name**

### Complexity

-   Time Complexity:  `O(n)`, where  `n`  is the total number of  `emails`.
-   Space Complexity:  `O(n)`

## Solution in Python

1. remove the first `'+'` by using one of the built-in string methods : `index`, `find`, `split`
   - `index` method: return the first position of a character in the string if the character exists in it, otherwise a `ValueError` is returned.
   - `find` method: return the first position of a character in the string if the character exists in it, otherwise `-1`  is returned.
  In my test, `index` seems **run faster** than `find`
   - `split` method: use `'+'` as a separator then take the first element.
2. remove all periods `'.'` by using the built-in string method `replace`, or using the combination of `split` and `join`
   - `replace` method: returns a copy of the string where all occurrences of a substring is replaced with another substring.
   - `split` the local name by the separator `'.'` then `join` elements to string without any separator.
In my tests, they have same speed.
3. **list or set?** We can use both list and set to store *canonical* addresses. We use *set* because it can remove dupplicate *canonical* addresses. But we can use *list* then convert it to *set* before count the number of email unique addresses.
In my tests, using *list* **run faster** than using *set*.
4. Python code: [unique_email.py](unique_email.py)
5. Unit test: [unique_email.py](../tests/unique_email.py)
-->