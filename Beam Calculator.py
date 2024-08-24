length = input("What is the room length?: ")
number_of_beams = input ("How many beams?: ")
width_of_beams = input("How wide are the beams?: ")

sub_total = int(length) - (int(number_of_beams)*int(width_of_beams))

total = int(sub_total) / (int(number_of_beams) + 1)

print(total)