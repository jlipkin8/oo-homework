"""
Parts 1-4
Create your classes and class methods here according to the practice instructions.
As you are working on Parts 1, 2, and 4, you can run the test python file
corresponding to that section to verify that you are completing the problem
correctly.
ex: python part_1_tests.py.
"""

class Student(object): 
    """Student class with first_name, last_name, and address attributes"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address 


class Question(object): 
    """Question class with question and correct_answer attributes"""

    def __init__(self, question, correct_answer): 
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self): 
        answer = raw_input(self.question + " ")
        #when run with part_2_tests.py 
        #use the following lines, instead of line 27git
        # print self.question, 
        # answer = raw_input(" >")
        if answer == self.correct_answer: 
            return True
        else: 
            return False


class Exam(object): 
    """Exam class with name and questions attributes"""

    def __init__(self, name): 
        self.name = name
        self.questions = []

    def add_question(self, question): 
        self.questions.append(question)

    def administer(self): 
        correct_count = 0 
        num_of_qs = float(len(self.questions))

        for question in self.questions: 
            if question.ask_and_evaluate(): 
                correct_count += 1 


        return correct_count/num_of_qs


class StudentExam(Exam): 
    """A subclass of Exam""" 

    def __init__(self, student, exam): 
        self.student = student
        self.exam = exam 
        self.score = None 

    def take_test(self): 
        self.score = super(StudentExam, self).administer()
        print "This student's score is {}".format(self.score)


class Quiz(Exam): 
    """A subclass of Exam"""

    def administer(self): 
        score = super(Quiz, self).administer()
        if score > .5: 
            return 1
        else:
            return 0


























