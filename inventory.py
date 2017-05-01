# Christopher Geier (cpg3rb)
import os


def path_exist(filename):
    if not os.path.exists(filename):
        a = open(filename, 'w')
        a.close()


def restock(filename, product, quantity):
    path_exist(filename)
    file = open(filename, 'r')
    final_file = open('_temp_inventory.csv', 'w')
    a = []
    prods = []
    for i in file:
        a.append(i.strip('\n').split(','))
        prods.append(i.split(',')[0])
    final = []
    new_quantity = quantity
    if product in prods:
        for i in a:
            if product == i[0]:
                i[1] = str(quantity + int(i[1]))
                new_quantity = int(i[1])
                final.append(i)
            else:
                final.append(i)
    else:
        while True:
            try:
                c = input('What is the price of ' + product + '? ')
                if float(c) > 0:
                    for i in a:
                        final.append(i)
                    final.append([product, quantity, c])
                    break
            except:
                continue
    for i in final:
        if len(i) == 3:
            final_file.write(str(i[0]) + ',' + str(i[1]) + ',' + str(i[2]) + '\n')
    file.close()
    final_file.close()
    os.remove(filename)
    os.rename('_temp_inventory.csv', filename)
    return new_quantity


def sell(filename, product, quantity):
    path_exist(filename)
    file = open(filename, 'r')
    final_file = open('_temp_inventory.csv', 'w')
    final = []
    new_quantity = quantity
    for i in file:
        i = i.strip('\n').split(',')
        if product == i[0]:
            if (int(i[1]) - quantity) == 0:
                new_quantity = 0
            elif (int(i[1]) - quantity) < 0:
                file.close()
                final_file.close()
                return None
            else:
                i[1] = str(int(i[1]) - quantity)
                new_quantity = i[1]
                final.append(i)
        else:
            final.append(i)
    file.close()
    for i in final:
        final_file.write(str(i[0]) + ',' + str(i[1]) + ',' + str(i[2]) + '\n')
    os.remove(filename)
    final_file.close()
    os.rename('_temp_inventory.csv', filename)
    return new_quantity
