cities= {'Delhi':'INDIA','London':'UK','Manchester':'UK','paris':'france','Indoor':'INDIA','seoul':'korea'}
d={}

for i in cities:
    if cities[i]in d:
        d[cities[i]].append(i)
    else :
        d[cities[i]]=[i]
print (d)