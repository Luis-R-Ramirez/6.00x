__author__ = 'luis'


s = "bobobbobobbobbobobog"

x = 0
aux = 0



for i in s:

    if aux == 2:
        if i == 'b':
            x = x + 1

            aux = 1
        else: aux = 0
    if aux == 1:
        if i == 'o':
            aux = 2

        if i != 'o':
           aux = 0

    if aux == 0:
        if i == 'b':
            aux = 1




print("Number of times bob occurs is: ", x )
