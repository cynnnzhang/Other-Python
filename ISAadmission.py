average = int(input("Enter the average of your top 8 grade 12 courses: "))

if average >= 90:
    advFunction = input("Have you taken Advanced Functions?: ")
    
    if advFunction == "yes":
        calcVectors = input("Have you taken Calculus and Vectors?: ")
        
        if calcVectors == "yes":
            english = input("Have you taken any Grade 12 U English: ")

            if english == "yes":
                fourU = input("Have you taken one other 4U course?: ")

                if fourU == "yes":
                    print("")
                    print("Spectacular! You pass the admission requirements to apply to")
                    print("University of Waterloo Computer Science!")
                    print("It's also good to know that taking Grade 11 Introduction to Computer Science")
                    print("and writing the Euclid Mathematics Contest is highly recommended.")

                else:
                    print("Sorry, you must take at least one other 4U course")

            else:
                print("Sorry you must take at least one Grade 12 U English")

        else:
            print("Sorry, you must take Calculus and Vectors")

    else:
        print("Sorry, you must take Advanced Functions first")

else:
    print("Sorry, your average is too low, you need at least low 90's to be considered")
