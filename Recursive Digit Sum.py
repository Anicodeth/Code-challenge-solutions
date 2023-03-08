def superDigit(n, k):
    
    def add_digits(string):
        if len(string) == 1:
            return string
        result = sum(int(s) for s in string)
        return add_digits(str(result))
    
    start = sum(int(s) for s in n) * k
    return add_digits(str(start))
