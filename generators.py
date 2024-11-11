#example for generators in python
def simpleGeneratorFun(A,B):
    yield 1   # file          
    yield 2  # str
    print(A+B)           
    yield 3            
for value in simpleGeneratorFun(4,5): 
    print(value)
    
#generator objects
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3 
# # x is a generator object
# x = simpleGeneratorFun()
# print(next(x))
# print(next(x))
# print(next(x))

# import argparse

# def simpleGeneratorFun(A, B):
#     yield 1
#     yield 2
#     print(A + B)
#     yield 3

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Simple Generator Example")
#     parser.add_argument("--A", type=int, help="First number")
#     parser.add_argument("--B", type=int, help="Second number")
    
#     args = parser.parse_args()

#     for value in simpleGeneratorFun(args.A, args.B):
#         print(value)

