# import sys 

# class Employee: 
#     def __init__(self, emp_id: int): 
#         if type(emp_id) != int: 
#             raise TypeError("Bad type: Employee id")
#         if emp_id <= 0: 
#             raise ValueError("Bad value for emp id")
#         self.emp_id = emp_id 
    
#     def get_emp_id(self) -> int: 
#         print("type(self):", type(self))
#         return self.emp_id 

# class Manager(Employee): 
#     def __init__(self, mng_emp_id: int, mng_team_size: int): 
#         if type(mng_team_size) != int: 
#             raise TypeError("Bad type: team size")
#         if mng_team_size <= 0: 
#             raise ValueError("Bad value: team size")
#         print("Manager:__init__():type(self):", type(self))
#         print("Manager.__init__():self.__dict__:", self.__dict__) # {}
#         Employee.__init__(self, mng_emp_id)
#         print("Manager.__init__():self.__dict__", self.__dict__) # {'emp_id': 27}
#         self.mng_team_size = mng_team_size
#         self.mng_emp_id = mng_emp_id
#         print("Manager.__init__():self.__dict__", self.__dict__) # {'emp_id': 27, 'mng_team_size': 15}

#     def get_team_size(self) -> int:
#         return self.mng_team_size

# def main(): 
#     M = Manager(27,15)
#     E = Employee(65)
#     print(E.get_emp_id())
#     print("main():M.__dict__", M.__dict__)
#     nr_members = M.get_team_size()
#     print("Mebers under manager M:", nr_members)
#     print("M.__dict__:", M.__dict__)

#     id_of_manager = M.get_emp_id() # Employee.get_emp_id(M)
#     idd_of_manager = M.mng_emp_id
#     print("ID of manager:", id_of_manager)
#     print("ID of manager:", idd_of_manager)
#     """
#     AttributeError: object of Manager has no attribute emp_id
#     """

class A:
    def __init__(self, _m , _n):
        self.m = _m
        self.n = _n

    def getmm(self):
        return self.m
    
    def getnn(self):
        return self.n

class B(A):
    def __init__(self, _m, _n, _p, _q):
        print("B.__init__():self.__dict__:", self.__dict__)
        A.__init__(self, _m , _n)
        print("B.__init__():self.__dict__:", self.__dict__)
        self.p = _p
        self.q = _q
        print("B.__init__():self.__dict__:", self.__dict__)

    def getp(self):
        return self.p
    
    def getq(self):
        return self.q

def main():
    b = B(1.1,2.2,100,200)
    print("b.__dict__", b.__dict__)
    print(b.getmm())
    print(b.getnn())

main()