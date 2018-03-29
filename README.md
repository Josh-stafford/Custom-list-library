## How to use

### Define List Object

variable_name = listlib.list(first item in list)

e.g. my_list = listlib.list('Orange')

### Push to List

list_object.push(item)

e.g. my_list.push('Yellow')

### Insert Item Into List

list_object.insert(index_value, item)

e.g. my_list.insert(1, 'Red')

### Remove Item From List

list_object.remove(index_value)

e.g. my_list.remove(2)

### Find Object in List

list_object.find(index_value)

e.g. my_list.find(1)

### Show Items in List

list_object.show()

e.g. my_list.show()

### Find Last Item in List

list_object.findLastNode()

e.g. my_list.findLastNode()

## Item Properties

Each item in the list is a node that has a data value and pointer object.

To get the value for an item in the list you must do 'item.data'

Do not touch the pointer value of each node as these are regulated by the library unless you are doing some sort of weird thingy.
