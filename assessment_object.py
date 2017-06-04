"""
"""
"""
Part 1: Discussion

1. 
What are the three main design advantages that object orientation can provide? 
Explain each concept.

 Three main advantages of object orientation:
 a. abstraction
 b. encapsulation
 c. polymorphism

 Abstraction: the developer doesn't need to know the details of what happens
 inside a method - only to understand the method signature and
 generally what the general behavior is, in order to use it. Complexity is out 
 of sight, out of mind. 

 Encapsulation: object orientation is modular, broken into sections that are
 self-contained, with all relevant info/code found in the same place.

 Polymorphism: pieces that should be interchangeable are interchangeable.

2. 
What is a class?
A class is a type of thing, and a template to create instances of that thing.
Classes are the blueprints for objects.

3. 
What is an instance attribute?
An instance attribute is a characteristic that is particular to a specific
instance of an object. (It's a post-it on the instance.)

4. 
What is a method?
A method is like a function for a class.

5. 
What is an instance in object orientation?
An instance is an instantiation of a class - a particular instance of the
class. So for the class development employee, I might have an instance which 
is a particular employee named "Danielle".

6. 
How is a class attribute different than an instance attribute?
Give an example of when you might use each.
For each instance of a class, the instance may get class attributes set
during instantiation, and the class attributes are shared among all instances
of the class.  An intance attribute is specific to a particular instance of
a class, and different instances likely have different values of an instance
attribute.

You would use a class attribute when all instances of the class are expected
to have the attribute, and when they are all expected to have the same value
of the attribute (though exceptions are possible).  

For example, a class attribute for the class employee could be employee hat. 
All employees get a hat on their first day. An instance attribute for the
employee could be the employee's door code. For each instance of an employee
a new door code is generated.

"""
"""
"""

# Parts 2 through 5:
# Create your classes and class methods


class Student(object):
    """A student"""

    def __init__(self, first_name, last_name=None, address=None, score=0):
        self.name = first_name
        self.lastname = last_name
        self.address = address
        self.score = score


class Question(object):
    """A question"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        """Ask a question and return True if the answer is correct"""
        student_answer = raw_input("> ")

        if student_answer == self.correct_answer:
            return True
        else:
            return False


class Exam(object):
    """An exam"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, correct_answer):
        """Adds a question to an exam"""
        exam_question = Question(question, correct_answer)
        self.questions.append(exam_question)

    def administer(self, student):
        score = 0

        for question in self.questions:
            if Question.ask_and_evaluate(question) == True:
                score += 1

        percentage_score = (float(score) / float(len(self.questions)) * 100)
        print "Your score is {}'.".format(percentage_score)

class Quiz(Exam):
    """Define Quiz object from Exam parent class. Return True for passing,
    False for failing."""

    def administer(self):
        percentage_score = super(Quiz, self).administer()

        if percentage_score >= 50:
            return True
        else:
            return False

def take_test(exam, student):
    """Allow student to take test and return score."""
  
    score = exam.administer(student)
    return score


def example(exam, student):
    """Create a sample exam and student, and take_test"""

    test = Exam(exam)
    student = Student(student)

    exam.add_question("What's 8+2?", "10")
    exam.add_question("What's 16+3?", "19")
    exam.add_question("What's 7+5?", "12")


    take_test(exam, student)
