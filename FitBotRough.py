print (str.center('WELCOME TO THE FITNESS ASSESSOR - A PROJECT BY MIHIR KAKKAR', 26))

print()

print (str.center("First things first, let me get to know you and your lifestyle!", 30))
name = input("What is your name?")

print()

if len(name) > 5:
  print("You have a long name!")
else:
  print("You have a very small name!") 

print()

print("Hello " + name + "! My name is FitBot, and I will be assisting you in your healthy journey!")
age = float(input("How old are you?"))

print("You are " + str(age) + " years old!")

print()

if age >= 18:
  print ("We need your weight to calculate your Body Mass Index. The Body Mass Index or BMI is a measure of body fat based on your weight in relation to your height.")
else:
  print ("This assessor is recommended for ADULTS: Proceed with caution")

print()

weight_lbs = float(input("How much do you weigh? (In pounds)"))
if weight_lbs > 500:
  print("Please enter a valid weight.")
elif weight_lbs < 0:
  print("Please enter a valid weight.")
else:
  print("Glad you are taking this important first step in becoming healthy " + name + "!")
weight_kgs = weight_lbs * 0.453592

print()

height_cm = float(input("So anyways, how tall are you? (In cm's)"))
if height_cm > 182:
  print ("Whoa! You are tall!")
else:
  print ("Nice!")

height_m = height_cm * 0.01
BMI = int((weight_kgs / height_m) / height_m)

print()

print("While I calculate your BMI, let's get to know each other - as friends!")

food = input("What is your favourite food?")
print("Ahh, " + str(food) + " used to be my favourite as well, back when I was a human. Now my favourite food is electricity! ZING! Oh, your BMI results are in! Hmmm, your BMI is actually " + str(BMI) + ".")

print()

if BMI < 24:
  print("You have a healthy BMI! Keep it up! Let us now look at the other aspects of your health, such as the amount of sleep you get, and how much water you drink!")
if BMI < 29:
  print("According to your BMI, it appears that you are actually overweight. No matter! Let's look at the other aspects of your health, such as the amount of sleep you get, and how much water you drink, to get a better understanding of where we can improve!")
else:
  print("According to your BMI, it appears that you are actually obese. No matter! Let's look at the other aspects of your health, such as the amount of sleep you get, and how much water you drink, to get a better understanding of where we can improve! ")

print()


