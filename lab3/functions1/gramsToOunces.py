def gramsToOunces(grams):
  return grams * 28.3495231

print(gramsToOunces(2))


def farenheitToCelcium(farenheit):
  farenheit = farenheit - 32
  return (5 / 9) * farenheit

print(farenheitToCelcium(60))

def solve(numheads, numlegs):
    if numlegs % 2 != 0 or numheads > numlegs // 2:
        return "No solution exists."

    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits

    if chickens < 0 or rabbits < 0:
        return "No solution exists."

    return chickens, rabbits

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(result)
