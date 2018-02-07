from random import randint 

# class wrapper for running Miller-Rabin primality test
class MillerRabin(object):
    # n is the number to test primality
    def __init__(self, n):
        self.n = n
        self.find_k()

    # n - 1 = 2^k * m
    def find_k(self):
        m = self.n - 1
        k = 0
        while m % 2 == 0:
            k += 1
            m //= 2
        self.k = k
        self.m = m

    # function to generate Miller-Rabin sequence for the given number a
    # seq empty if n is even
    def generate_mr_seq(self, a):
        seq = []
        a = pow(a, pow(2, 0)*self.m)
        for i in range(self.k):
            a %= self.n
            seq.append(a)
            a **= 2
        return seq

    # checks if the given number a is a witness for primality of n
    def is_witness(self, a):
        seq = self.generate_mr_seq(a)
        if not seq:
            return False
        elif seq[0] == 1 or self.n-1 in seq:
            return True
        else:
            return False

    # assuming n is odd, finds liars that assert n is prime
    def find_liars(self):
        liars = [i for i in range(1, self.n) if self.is_witness(i)]
        return liars

    # computes the ratio of liars between 1 to n-1
    def liar_ratio(self):
        liars = self.find_liars()
        return len(liars)/(self.n - 1)

    # runs Miller-Rabin primality test for num_trial times
    # probability of being prime is 1 - 0.25^num_trial
    def is_prime(self, num_trial):
        def one_trial():
            a = randint(1, self.n - 1)
            return self.is_witness(a)

        if self.n % 2 == 0:
            return False

        for i in range(num_trial):
            if not one_trial():
                return False
        return True

def is_prime(n, num_trial = 10):
    mr = MillerRabin(n)
    if mr.is_prime(num_trial):
        print("Probably prime with probability " + str(100*(1 - 0.25**num_trial)) + "%")
    else:
        print("Defintely composite")
