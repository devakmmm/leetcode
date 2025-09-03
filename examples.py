def add_expense(expenses, amount, category):
    expenses.append({'amount': amount})
    #the append function calls the dictionary amount as key and amount as value

#     filter(my_function, my_list)
# filter() takes a function as its first argument and an iterable as its second argument. It returns an iterator, which is a special object that enables you to iterate over the elements of a collection, like a list.

# The result of the example above is an iterator containing the elements of my_list for which my_function returns True. You can convert this iterator to a list using the list() function, as shown in the example.