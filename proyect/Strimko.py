import sys
from constraint import Problem, AllDifferentConstraint

matrixOfStrimko = None

class Matrix:
    
    def __init__(self,size):
        self.size = size
        #matrix of the game
        self.matrix = [[0 for x in range(self.size)] for y in range(self.size)]
        # routes where we are going to sav
        self.routes = []
        
    def addRoute(self,route):
        if len(self.routes) == self.size:
            return
        if route.getRouteSize() > self.size:
            return
        self.routes.append(route)
        
    def printMatrix(self):
        print(self.matrix)
        
    def printRoutes(self):
        for i in range(self.size):
            print(self.routes[i].printRoute())
        
           
class Route:
    
    #elements are a list of boxes
    def __init__(self,elements):
        self.elements = elements
        
    def printRoute(self):
        for i in range(len(self.elements)):
            print(self.elements[i])
        
    def getRouteSize(self):
        return len(self.elements)
    
    
def solve():
        problem = Problem()
        
        size = matrixOfStrimko.size + 1
        
        # Define the variables:  rows of x variables rangin in 1...x
        # x = tam of the matrix
        for i in range(1, size):
            problem.addVariables(range(i * 10 + 1, i * 10 + size), range(1, size))
                     
        #Each row has different values
        for i in range(1, size):
            problem.addConstraint(AllDifferentConstraint(), range(i * 10 + 1, i * 10 + size ))
            
        # Each colum has different values
        for i in range(1, size):
            problem.addConstraint(AllDifferentConstraint(), range(10 + i, 10 * size + i, 10))
            
        #Each route has different values
        for i in range(0, size - 1):
            problem.addConstraint(AllDifferentConstraint(),matrixOfStrimko.routes[i].elements)
        
        return problem.getSolutions()
         
          
def getRouteFromUserImput(size):
    
    elementsOfRoute = []
    #get the elements of the route from console
    for i in range(size):
        inputOfBox = input()
        inputOfBox = inputOfBox.split()
        #convert it to interger
        box = inputOfBox[0] + inputOfBox[1]
        #store box as Object into elements of Route
        elementsOfRoute.append(int(box))
        
    return elementsOfRoute


def printSolutions(solutions):
    for solution in solutions:
        for i in range(1, matrixOfStrimko.size + 1):
            for j in range(1, matrixOfStrimko.size + 1):
                index = i * 10 + j
                sys.stdout.write("%s " % solution[index])
            print("")
        print("")
    

def main():
    global matrixOfStrimko
    
    sizeOfMatrix = int(input())
    
    if sizeOfMatrix <2:
        print("Invalid input: the size of the strimko must be 2 or higher")
        return
    
    matrix = Matrix(sizeOfMatrix)
    
    for i in range(sizeOfMatrix):
        matrix.addRoute(Route(getRouteFromUserImput(sizeOfMatrix)))
        input()
        
    matrixOfStrimko = matrix
    
    solutions = solve()
    #print the len of the solutions of the strimko
    print(len(solutions))
    
    #in case of show the matrixes with the posible solutions
    #printSolutions(solutions)
    
    

if __name__ == "__main__":
    main()
    



    
    