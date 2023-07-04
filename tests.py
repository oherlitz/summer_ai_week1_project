people = {
            1 : "dxfcjgkhljiok",
            2 : 'dfghkj',
                }
def counter(dict):
    count = 0
    for key,value in dict.items():
        count += 1
    return count
y = counter(people)
print(y)