def InttoRoman(num):
  D = {1:"I", 4: "IV", 5:"V", 9:"IX", 10:"X", 40: "XL", 90:"XC",
              50:"L", 100:"C", 500:"D", 1000:"M", 400:"CD", 900:"CM"}

          res = ''
          A = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

          while num > 0:
              if num in D:
                  res += D[num]
                  break
              for val in A:
                  if num >= val:
                      num -= val
                      res += D[val]
                      break

          return res        
print(InttoRoman(450))
==>TC=O(n) or O(logn)
