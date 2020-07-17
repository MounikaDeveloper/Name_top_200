import os
def get_names_list(filename):
    list = []
    dir_name='C:/Users/mouni/Desktop/topnames/'
    file = os.path.join(dir_name + filename)
    for x in open(file):
        data = x.rstrip('\n')
        list.append(data)
    return list

def check_name(name,name_list):
    try:
        rank=name_list.index(name)
        return rank+1
    except ValueError:
        return None

def main():

    print("Enter a name to see if it is a popular girls or boys name.\n")
    while True:
        name=input('Enter a name to check, or "stop" to stop:')
        if name.lower()=='stop':
            return False
        name=name.capitalize()
        name_list=get_names_list('girlsNames')
        rank=check_name(name,name_list)
        if rank:
            print(name + "\tis a popular girls name and is ranked:" + str(rank))
        else:
            print(name + "\tis  not a popular girls name" )
        name_list = get_names_list('boysNames')
        rank = check_name(name, name_list)
        if rank:
            print(name + "\tis a popular boys name and is ranked:\n" +str(rank))
        else:
            print(name + "\tis  not a popular boys name\n")
main()