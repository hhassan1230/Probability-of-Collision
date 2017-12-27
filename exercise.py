def probability_of_collision(car_1, car_2):
    # car_1 and car_2 will each be strings whose value will either be 
    # "L" for left, "S" for straight, or "R" for right.
    collisions = {
        "L": {
            "L": 0.5,
            "S": 0.25,
            "R": 0.1
        },
        "S": {
            "L": 0.25,
            "S": 0.02,
            "R": 0.1
        },
        "R": {
            "L": 0.1,
            "S": 0.1,
            "R": 0.01
        }
    }
    probability = collisions[car_1][car_2] # you should change this value based on the directions.
    
    return probability


# This function is used to test the correctness of your code. You shouldn't
# touch any of the code below here (but feel free to look through it to
# understand what "correct" looks like).
def test():
    num_correct = 0
    
    p1 = probability_of_collision("L", "L")
    if p1 == 0.5:
        num_correct += 1
    
    p2 = probability_of_collision("L", "R")
    if p2 == 0.1:
        num_correct += 1
    
    p3 = probability_of_collision("L", "S")
    if p3 == 0.25:
        num_correct += 1
    
    p4 = probability_of_collision("S", "R")
    if p4 == 0.1:
        num_correct += 1
    
    print("You got", num_correct, "out of 4 correct")
    
test()