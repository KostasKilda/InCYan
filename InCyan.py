import json

# The received dynamic payload
json_payload = '{ "title": "stock count", "xtitle": "asset", "ytitle": "count", "items": [ {"chairs": 20}, {"tables": 5}, {"stands": 7}, {"lamps": 8}, {"cups": 10} ]}'

payload = json.loads(json_payload)


emptyTitleSpace = '                               '

# Underlining for the title
Underline = "_" * len(payload['title'])
print("\n" + emptyTitleSpace + payload['title'])
print(emptyTitleSpace + Underline)

# Dynamic underline for the YTitle
Underline = "_" * len(payload['ytitle'])
print(payload['ytitle'])
print(Underline, "\n")

# Converting the dictionary of items to an array
ListOfItems = [[key, value] for item in payload['items'] for key, value in item.items()]

# Finding the maximum numerical value of the list
maxValue = (max(ListOfItems, key=lambda x: x[1]))
maxValue = maxValue[1]

# Dynamically obtaining the spacing required between items
spacingList = [len(payload['ytitle'])]
for i in range(len(ListOfItems)):
    spacingList.append(1 + len(ListOfItems[i][0]))


# Printing the asci stars
printRange = maxValue//10
for i in range(9, 0, -1):
    for k in range(len(ListOfItems)):
        print(spacingList[k] * " ", end="")
        if(k>=1):
            print(" ", end='')
        if(ListOfItems[k][1]>= i*printRange):
            print("*", end="")
        else:
            print(" ", end="")
    print(end="\n")

# Printing the items
print(len(payload['ytitle']) * " ",end="")
for i in range(len(ListOfItems)):
    print(ListOfItems[i][0], end="   ")

# Printing the xtitle
print("")
print(len(payload['ytitle']) * " ",end="")
for i in range(len(ListOfItems)):
    print(" " * spacingList[i], end=" ")
print(payload['xtitle'])

# Underlining the xtitle
print(len(payload['ytitle']) * " ",end="")
for i in range(len(ListOfItems)):
    print(" " * spacingList[i], end=" ")
print("_" * len(payload['xtitle']))
