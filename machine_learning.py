class MachineLearning:
    def __init__(self,name,category):
        self.name=name
        self.category=category
        
    def getname(self):
        return self.name
        
    def getcategory(self):
        return self.category
        
    def print(self):
        print("Name:",self.name)
        print("Category:",self.category)

class Supervised(MachineLearning):
    def __init__(self,name,category):
        #YOUR CODE GOES HERE
        super().__init__(name,category)
    
    def type(self):
        #YOUR CODE GOES HERE
        self.print()
        print('Supervised Learning Algorithm')

class Unsupervised(MachineLearning):
    def __init__(self,name,category):
        #YOUR CODE GOES HERE
        super().__init__(name,category)
    
    def type(self):
        #YOUR CODE GOES HERE
        self.print()
        print('Unsupervised Learning Algorithm')


obj1=Supervised("Logistic Regression", "Classification Algo")
obj1.type()
obj2=Unsupervised("Kmeans", "Clustering Algo")
obj2.type()