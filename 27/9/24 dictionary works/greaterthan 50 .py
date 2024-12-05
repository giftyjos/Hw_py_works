orginal_dict={
    'apple': 100,
    'banana': 30,
    'cherry':75,
    'date': 45,
    'mango': 60
} 
filtered_dict={key:value for key,value in orginal_dict.items() if value>50}

print(filtered_dict)