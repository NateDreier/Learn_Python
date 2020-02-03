# Loop exercises

# function that takes in a list and returns the count of numbers are divisible by 10
def div_by_ten(nums):
    x = 0
    for i in nums:
        if i % 10 == 0:
            x += 1  
    return(x)

# function that teakes a list of names and returns that same list of names but with hello before each name
def namuh(names):
    greetings = []
    for i in range(len(names)):
        greetings.append("Hello, " + names[i])
    return(greetings)


print(div_by_ten([10, 15, 20, 10, 30, 45, 32]))
print(namuh([nate, sophie, lily, emma]))