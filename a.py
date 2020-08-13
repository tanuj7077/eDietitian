import sys

def calcPossibilities(items, maxCal, maxP, maxC, maxF, maxIntake, Map,reqMacros,Possibilities,macros,cal,p,c,f,item,count,maxItems):
    #global count
    #global Possibilities
    #global macros
    #global maxItems
    #global cal, p, c, f, item
    #count[0] += 1
    if (maxCal < -50 or maxP < -15 or maxC < -20 or maxF < -10):
        return 0
    if (maxCal <= 0 or items <= 0):
        if ((maxP > -15 and maxP < 15) and (maxC > -20 and maxC < 20) and (maxF > -10 and maxF < 10) and (maxCal > -50 and maxCal < 50)):
            #print(count,Map)
            Possibilities[count[0]] = Map
            macros[count[0]] = [abs(maxP - reqMacros[1]), abs(maxC - reqMacros[2]), abs(maxF - reqMacros[3]),
                             abs(maxCal - reqMacros[0])]
            maxItems[0] = max(maxItems[0],len(Map))
            count[0]+=1
            return 0
        else:
            return -sys.maxsize

    if (cal[items - 1] > maxCal):
        return calcPossibilities(items - 1, maxCal, maxP, maxC, maxF, maxIntake.copy(), Map.copy(),reqMacros.copy(),Possibilities,macros,cal,p,c,f,item,count,maxItems)
    Excluding = calcPossibilities(items - 1, maxCal, maxP, maxC, maxF, maxIntake.copy(), Map.copy(),reqMacros.copy(),Possibilities,macros,cal,p,c,f,item,count,maxItems)
    if (maxIntake[items - 1] - 1 >= 0):
        maxIntake[items - 1] -= 1
        if (item[items - 1] in Map):
            Map[item[items - 1]] += 1
        else:
            Map[item[items - 1]] = 1
        Including = cal[items - 1] + calcPossibilities(items, maxCal - cal[items - 1], maxP - p[items - 1],
                                                       maxC - c[items - 1], maxF - f[items - 1], maxIntake.copy(), Map.copy(),
                                                        reqMacros.copy(),Possibilities,macros,cal,p,c,f,item,count,maxItems)
        Map[item[items - 1]] -= 1
        return max(Including, Excluding)
    return Excluding

def calcBest(Possibilities,macros,ans,maxItems):
    for x in Possibilities:
        if len(Possibilities[x])==maxItems[0]:
            ans[x]=Possibilities[x]


item = ["Egg Whites", "Whole Eggs", "Chicken", "Whey", "Seeds", "Oats", "Almond", "Curd", "Paneer", "PeanutButter"]
maxIntake = [15, 4, 5, 2, 2, 4, 1, 2, 2, 3]
p = [4, 6, 10, 25, 9, 6, 3, 11, 9, 7]
c = [0, 1, 0, 2, 18, 35, 3, 4, 1, 7]
f = [0, 5, 2, 2, 16, 5, 6, 4, 10, 16]
cal = [17, 78, 70, 120, 218, 205, 70, 100, 130, 186]
items = len(item)
maxCal = 1503
maxP = 150
maxC = 120
maxF = 47
count = [0]  # no. of calls
maxItems = [0]
Map = {}  # food : quantity
Possibilities = {}  # count : Map  i.e all combinations
macros = {}  # count : list  i.e each combination macros
reqMacros = [maxCal, maxP, maxC, maxF]
calcPossibilities(items, maxCal, maxP, maxC, maxF, maxIntake, Map,reqMacros,Possibilities,macros,cal,p,c,f,item,count,maxItems)
# print(Possibilities)
ans={}
calcBest(Possibilities,macros,ans,maxItems)
'''for k in Possibilities:
    print(k, Possibilities[k])'''
for k in ans:
    print(k, ans[k])
#print(len(ans))
print(maxItems[0])