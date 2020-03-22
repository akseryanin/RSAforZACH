import random

class RSAalg(object):

    def _isPrime(self, n):
        cnt = 2
        while cnt * cnt <= n:
            if not (n % cnt):
                return False
            cnt += 1
        return True

    def _get_prime(self, start, finish):
        n = random.randint(start, finish)
        while not self._isPrime(n):
            n += 1
        return n

    def _gcd(self, a, b):
        if not a:
            return b
        return self._gcd(b % a, a)

    def _extended_euclid(self, a, b):  # (x, y, d)
        # вычисление a * *x + b * *y = gcd(a, b) = *d
        if (b == 0):
            return (1, 0, a)
        x2, x1, y2, y1 = 1, 0, 0, 1
        while (b > 0):
            q = a // b
            r = a - q * b
            x = x2 - q * x1
            y = y2 - q * y1
            a = b
            b = r
            x2 = x1
            x1 = x
            y2 = y1
            y1 = y
        d = a
        x = x2
        y = y2
        return (x, y, d)

    def _inverse(self, a, n):
        # вычисление обратного элемента по модулю n
        x, y, d = self._extended_euclid(a, n)
        if (d == 1):
            return x
        return 0

    def __init__(self):
        self._p = self._get_prime(1e4, 1e5)
        self._q = self._get_prime(1e4, 1e5)
        while self._p == self._q:
            self._q = self._get_prime(1e4, 1e5)
        self._n = self._p * self._q
        self._fi = self._n - self._p - self._q + 1
        self._e = [3, 5, 17, 257, 65537][random.randint(0, 4)]
        while self._gcd(self._e, self._fi) != 1:
            self._e = [3, 5, 17, 257, 65537][random.randint(0, 4)]
        self._d = self._inverse(self._e, self._fi)
        self.open_key = (self._e, self._n)
        self._close_key = (self._d, self._n)

    def encrypt_int(self, digit):
        return pow(digit, self._e, self._n)

    def decrypt_int(self, digit):
        return pow(digit, self._d, self._n)

    def encrypt_string(self, s):
        return [self.encrypt_int(ord(elem)) for elem in s]
    def decrypt_string(self, arr):
        ans = ''
        for elem in arr:
            ans += chr(self.decrypt_int(elem))
        return ans



