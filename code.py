import copy


class term:
    def __init__(self, term_str):
        if term_str == "":
            self.factor = 0
            self.pow = 0
        else:
            temp = term_str.split("x^")
            self.factor = int(temp[0])
            self.pow = int(temp[1])

    def __str__(self):
        out = ""
        if(self.factor > 0):
            out += "+"
        out += str(self.factor)
        out += "x^"
        out += str(self.pow)
        return out
 
    def __lt__(self, other):
        return self.pow > other.pow

    def __mul__(self, other):
        result = term("")
        result.pow = self.pow + other.pow
        result.factor = self.factor * other.factor
        return result

    # def __add__(self, other):
    #     result = term("")
    #     result.pow = self.pow
    #     result.factor = self.factor + other.factor
    #     return result

    # def __sub__(self, other):
    #     result = term("")
    #     result.pow = self.pow
    #     result.factor = self.factor - other.factor
    #     return result

class polynomial:
    def __init__(self, input):
        self.terms = []
        if input != "":
            delimiter = ["+", "-"]
            temp = ""
            for char in input:
                if char in delimiter:
                    if temp != "":
                        self.terms.append(term(temp))
                    temp = char
                else:
                    temp += char
        
            self.terms.append(term(temp))
            self.simplify()

    def simplify(self):
        self.terms.sort()
        i = 0
        while i < len(self.terms):
            j = i+1
            while j < len(self.terms) and self.terms[i].pow == self.terms[j].pow:
                self.terms[i].factor += self.terms[j].factor
                self.terms.pop(j)

            if self.terms[i].factor == 0:
                self.terms.pop(i)
            else:    
                i = j

    def __str__(self):
        out = ""
        for t in self.terms:
            out += str(t)
        return out

    def __mul__(self, other):
        result = polynomial("")
        for t1 in self.terms:
            for t2 in other.terms:
                result.terms.append(t1 * t2)

        result.simplify()
        return result

    def __add__(self, other):
        result = polynomial("")
        for t in self.terms:
            result.terms.append(copy.deepcopy(t))
        for t in other.terms:
            result.terms.append(copy.deepcopy(t))
        result.simplify()
        return result

    def __sub__(self, other):
        result = polynomial("")
        for t in self.terms:
            result.terms.append(copy.deepcopy(t))
        for t in other.terms:
            temp = term("")
            temp.pow = t.pow
            temp.factor = -t.factor
            result.terms.append(temp)

        result.simplify()
        return result


p1 = polynomial(input())
p2 = polynomial(input())

inpt = input()
while inpt != "exit":
    if inpt == "+":
        res = p1 + p2
    elif inpt == "-":
        res = p1 - p2
    elif inpt == "*":
        res = p1 * p2
    else:
        break
    print(res)
    inpt = input()


# p3 = p1 * p2
# p4 = p1 + p2
# p5 = p1 - p2

# print("P1 :")
# for t in p1.terms:
#     print(t)

# print("P2 :")
# for t in p2.terms:
#     print(t)

# print("P3 :")
# for t in p3.terms:
#     print(t)

# print("P4 :")
# for t in p4.terms:
#     print(t)

# print("P5 :")
# for t in p5.terms:
#     print(t)

# print(p1)
# print(p2)
# print(p3)
# print(p4)
# print(p5)