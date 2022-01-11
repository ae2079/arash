class term:
    def __init__(self):
        self.factor = 0
        self.pow = 0

    def fit(self, term_str):
        temp = term_str.split("x^")
        self.factor = int(temp[0])
        self.pow = int(temp[1])

    def __lt__(self, other):
        return self.pow > other.pow

    def __mul__(self, other):
        result = term()
        result.pow = self.pow + other.pow
        result.factor = self.factor * other.factor
        return result

    def __add__(self, other):
        result = term()
        result.pow = self.pow
        result.factor = self.factor + other.factor
        return result

    def __sub__(self, other):
        result = term()
        result.pow = self.pow
        result.factor = self.factor - other.factor
        return result

class polynomial:
    def __init__(self):
        self.terms = []
    
    def fit(self, input):
        delimiter = ["+", "-"]
        temp = ""
        for char in input:
            if char in delimiter:
                if temp != "":
                    t = term()
                    t.fit(temp)
                    self.terms.append(t)
                temp = char
            else:
                temp += char

        t = term()
        t.fit(temp)
        self.terms.append(t)
        self.simplify()

    def simplify(self):
        self.terms.sort()
        i = 0
        while i < len(self.terms):
            j = i+1
            while j < len(self.terms) and self.terms[i].pow == self.terms[j].pow:
                self.terms[i].factor += self.terms[j].factor
                self.terms.pop(j)
            i = j

    def __mul__(self, other):
        result = polynomial()
        for t1 in self.terms:
            for t2 in other.terms:
                result.terms.append(t1 * t2)

        result.simplify()
        return result



p1 = polynomial()
p1.fit(input())
p2 = polynomial()
p1.fit(input())

#p3 = p1 * p2
print("P 1 :")
for t in p1.terms:
    print("f :", t.factor, "p :", t.pow)

print("P 2 :")
for t in p2.terms:
    print("f :", t.factor, "p :", t.pow)

# print("P 3 :")
# for t in p3.terms:
#     print("f :", t.factor, "p :", t.pow)
