import pandas as pd 

#Create Data
student_data = {
    'ID': [1, 2, 3, 4],
    'Name': ['Nida', 'Afreen', 'Beauty', 'Golu'],
    'Age' : [23,22,21,24],
    'Dept' : ['MCA','BCA','BTECH','MBA']
   
}

student_address = {
    'ID' : [3, 4, 5, 6],
    'City' : ['Dehri','Gaya','Varanashi','Bhoplal'],
    'State' : ['Bihar','UP','Bihar','MP'],
    'PIN CODE' : [2010, 2310, 2431, 2466]
}

#Convert dictionaries to DataFrames
df1 = pd.DataFrame(student_data)
df2 = pd.DataFrame(student_address)

#INNER JOIN 
inner_join = pd.merge(df1, df2, on='ID', how='inner')
print("Inner Join:\n", inner_join)

#LEFT JOIN 
left_join = pd.merge(df1, df2, on='ID', how='left')
print("Left Join:\n", left_join)

#RIGHT JOIN 
right_join = pd.merge(df1, df2, on='ID', how='right')
print("Right Join:\n", right_join)

#OUTER JOIN 
outer_join = pd.merge(df1, df2, on='ID', how='outer')
print("Outer Join:\n", outer_join)
