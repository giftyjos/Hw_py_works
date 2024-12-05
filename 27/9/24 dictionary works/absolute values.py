my_dict={'a':-1,'b': 2,'c':-3,'d':4}

abs_dict={key: abs(value) for key,value in my_dict.items()}

print(abs_dict)