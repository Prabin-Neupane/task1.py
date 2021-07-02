 #to print min no if both input are odd else print max no
def numbers(a,b):
    if a%2 == 0:
        return max(a,b)
    else:
        return min(a,b)

print(numbers(90,8))