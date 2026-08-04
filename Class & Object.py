# CLASS AND OBJECTS
'''it is code reusability
code gets structure
for high complex and automation
it undercomes from the topic is OOPS=Object Oriented Programong Structural language '''

class student: # this line is assign of class 
    def pen(self): # def pen(sachin):                  
        print("u have to write")
    def book(self):                # these all are methods
        print("ready to read")
saran=student() # Here the oject is saran it is used to give the access ticket to that class
sachin=student()
sachin.pen() #To access the class methos through the object here sachin.pen
# here python will execute like this sachin.pen(sachin) because the pen method knows who can access the pen method(objects)

#CONSTRUCTOR IN CLASS AND OBJECT
class college:
    def __init__(self,student_name,student_department): 
        # here constructor is runs first because it is predefind python function
        self.name=student_name
        self.department=student_department
    def application(self):
        print(f"student_name: {self.name} student_department: {self.department}")    
saran=college("saran","Artificial Inteligence") 
'''When we pass the arguments through the class 
it will accessable by the entire methods which we created in that particular class '''      
saran.application() #Here i just call the function it will fetch the arguments from class itself


# ANOTHER EXAMPLE FOR CONSTRUCTOR IN CLASS AND OBJECT
class employee:
    def __init__(self,name,addhar_no):
        self.name1=name # stored once
        self.addharno=addhar_no # stored once
    def employee_id(self):
        print(f"employee_name: {self.name1} employee_addharno: {self.addharno}")
    def open_bankaccount(self):
        print(f"bank accopunt open for {self.name1} and his addhar number is {self.addharno}")
em1=employee("saran",792597008040)
'''When we pass the arguments through the class 
it will accessable by the entire methods which we created in that particular class '''
em2=employee("sachin",897097008040)
em1.employee_id() # Here i just call the function it will fetch the arguments from class itself
em1.open_bankaccount() # Here i just call the function it will fetch the arguments from class itself

# ANOTHER EXAMPLE FOR CLASS AND OBJECT WITHOUT CONSTRUCTOR
class mathtools:
    def add(self,a,b):
        return(a+b)
    def square(self,n):
        return(n*n)  
    def cube(self,n):
       return(n*n*n) 
n1=mathtools()
print(n1.add(5,8))
print(n1.square(6))
print(n1.cube(9))             




