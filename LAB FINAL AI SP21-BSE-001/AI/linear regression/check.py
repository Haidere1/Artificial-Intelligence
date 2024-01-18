import numpy as np
def sum():
    a=np.array([1,2,3,4,5,6,7,8,9,10])
    b=np.array([1,2,3,4,5,6,7,8,9,10])
    #ok emaan waheed this np.arrange will create an array containing numbers from 1-50
    #the variable random_no will hold the random number selected from the array
    #by using np.random.choice(the name of the array ok?)
    array=np.arange(1,51)
    random_no=np.random.choice(array)
    sum=np.add(a,b)
    mltply=np.multiply(a,b)
    print(sum)
    print(mltply)
    print(random_no)

sum()