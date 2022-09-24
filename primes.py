"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number entered is not valid")
    else:
        list = [2]

        if number_of_primes > 1:
            list.append(3)

        if number_of_primes > 2:
            n = 5
            while len(list) < number_of_primes:
                if (n + 1) % 6 == 0 or (n - 1) % 6 == 0:
                    if len(list) < 5:
                        list.append(n)
                    else:
                        multiple = True
                        for x in list[0:4]:
                            if n % x == 0:
                                multiple = False
                                break
                        if multiple == True:
                            list.append(n)

                n += 1

        return list
