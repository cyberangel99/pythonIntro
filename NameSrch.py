#Mary Green
#4/15/2018
#Unit 9
#NameSrch.py
#Creating an array to search for a specific name


def main():

   SearchName=input('Enter a name to search:')
   names = ['Ava Fischer', 'Bob White', 'Chris Rich', 'Danielle Porter', 'Gordon Pike',
            'Hannah Beauregard', 'Matt Hoyle', 'Ross Harrison', 'Sasha Ricci', 'Xavier Adams']
   TotalNames=len(names)
   NameSrch=binarySearch(names, SearchName, TotalNames)
   if NameSrch == -1:
    print('Name not found with the query: ', SearchName)
   else:
    print('Name found at position: ', NameSrch)

def binarySearch(arr, value, total):
    index = 0
    position = -1
    found = False
    while index < total and found == False:
        if arr[index] == value:
            position = index
            found = True
        index = index +1
    return position



main()
