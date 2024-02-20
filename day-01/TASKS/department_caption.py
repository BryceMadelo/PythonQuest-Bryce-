#user name
name = input("Enter your name: ")

#AWS CLoud Club Department
department = input("Enter the AWS Cloud Clud department you belong: ")

#Galaxy
galaxy = input("Specify the galaxy you belong: ")

print("Your Department's DP Blast Caption:")
#Output
dpBlast = " 🚀Deploying...I'm {}, representing the department of {}. I'm thrilled to commence our expedition into the vast and uncharted realm of the {} Galaxy. Together, we'll navigate this exciting frontier of technology! 🌌🌟💻 ".format(name, department, galaxy)
print(dpBlast)