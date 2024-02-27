import random

class University:
    def __init__(self, name, location, courses_offered):
        self.name = name
        self.location = location
        self.courses_offered = courses_offered

    def get_info(self):
        return f"Welcome to {self.name} located in {self.location}. \n\nWe offer courses in {', '.join(self.courses_offered)}."

    def get_financial_aid_info(self):
        return "We offer various financial aid options including scholarships, grants, and student loans."

def welcome_message():
    print("Welcome to University Admission Chatbot!")
    print("Hello, My name is Alexa.")
    print("I can help you with the admission process. Let's get started.")

def get_personal_details():
    print("\nPlease provide some personal details:")
    name = input("What is your Name: ")
    age = input("What is your Age: ")
    address = input("Lastly, your Address: ")
    return name, age, address

def get_academic_details():
    print("\nGreat! Now, let's gather some academic details:")
    puc_marks = input("What is your 2nd PUC or 12th marks: ")
    cet_rankings = input("What is your CET Rankings: ")
    
    extracurriculars = input("Extracurricular Activities (if any): ")
    return cet_rankings, puc_marks, extracurriculars

def evaluate_admission_eligibility(cet_rankings, puc_marks):
    cet_rank = 20000
    puc_score = 75

    if float(cet_rankings) <= cet_rank and int(puc_marks) >= puc_score:
        return True
    else:
        return False

def admission_process(university):
    welcome_message()
    name, age, address = get_personal_details()
    cet_rankings, puc_marks, extracurriculars = get_academic_details()

    if evaluate_admission_eligibility(cet_rankings, puc_marks):
        print(f"\nCongratulations, {name}! You are eligible for admission.")
        print(university.get_info())
        financial_aid = input("\nWould you like information about financial aid? (yes/no): ").lower()
        if financial_aid == "yes":
            print(university.get_financial_aid_info())
        else:
            print("\nFeel free to ask any other questions.")
        print("We will review your application and get back to you soon.")
        print("Thank you for your interest in our institution.")
    else:
        print(f"\nSorry, {name}! You do not meet the admission criteria.")
        print("You may consider improving your academic credentials and reapplying in the future.")

if __name__ == "__main__":
    university = University("Sahyadri college of Engineering and Managment", "Mangaluru city", ["\n1.Computer Science(CSE) \n2.CSE: AIML \n3.Mechanical Engg \n4.Electrical Engg \n5.Business Administration"])
    admission_process(university)