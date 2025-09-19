import numpy as np

dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]

values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7), 
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]
           
arr = np.array(values, dtype = dtypes)
print ("\nArray sorted by names:\n",
            np.sort(arr, order = 'name'))
            
print ("Array sorted by graduation year and then cgpa:\n",
                np.sort(arr, order = ['grad_year', 'cgpa']))
