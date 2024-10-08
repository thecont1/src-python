class AnyNumber:
    def __init__(self, n):
        # Pick a number, any number
        self.n = n

    # Decorator function
    def printout(func):

        def wrapper(self):
            if self.n is None:
                return f"\n कृपया इनपुट देने से पहले थोड़ा सोचें। Love, {self.__class__.__name__}() \n"
            else:
                return f"\n*****  {func(self)}  *****\n"
        
        return wrapper

    @printout
    def expand(self):
        # Function that takes a numeral as input and prints corresponding words
        words = ['0 (शून्य)', '1 (एक)', '2 (दो)', '3 (तीन)', '4 (चार)', 
                '5 (पांच)', '6 (छः)', '7 (सात)', '8 (आठ)', '9 (नौ)']
        numerals = list(str(self.n))        # Input number may be either string or int
        text = ""
        for n in numerals:
            text += f"{words[int(n)]}  "
        return text[:-2]                    # Remove 2 extra spaces at the end

    def __str__(self):
        return self.expand()


class Even(AnyNumber):
    def __init__(self, n):
        # Pick a number, any EVEN number
        super().__init__(n if int(n) % 2 == 0 else None)


class Prime(AnyNumber):
    def __init__(self, n):
        # Pick a number, any PRIME number
        super().__init__(n if self.__isPrime(n) else None)

    def __isPrime(self, n):
    # Test if the input number is prime or not
        if int(n) < 2:
            return False
        if int(n) == 2:
            return True
        if int(n) % 2 == 0:
            return False
        for i in range(3, (int(n) + 1) // 2, 2):
            if int(n) % i == 0:
                return False
        return True


# Input: A number either as type string or int
# Output: Each digit in words OR error depending on the sub/class
number = 97453

print(AnyNumber(number))
print(Even(number))
print(Prime(number))
