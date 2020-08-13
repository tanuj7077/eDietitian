from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from main.models import extendUser,food
import sys
import ast


def main(request):
    foods= food.objects.all()
    u = User.objects.get(username=request.user.username)#user instance(currently logged in)
    s = ""
    try:
        e = extendUser.objects.get(user = u)#if extendUser exists
    except: #if new user or first time setting macros
        if request.POST.get("sProgram"):
            setProgram(foods, u, request)
            return redirect('/main')
            
        s = s+"Your Macronutrients not set currently. Calculate your macronutrients from the calculator given here."
        dtStatus = "You cannot select foods until the macro-nutrients are calculated"
        #user = extendUser(user=u, macroStatus=s)
        #user.save()
        return render(request, "mainPage.html", {'macroStatus': s,'vis':0, 'dtStatus':dtStatus})
    else: #if not new user
        if request.POST.get("sProgram"):
            setProgram(foods, u, request)
            return redirect('/main')
            #resetDiet(because macros are set again and old diet will not work)==========================
            
        if request.POST.get("sDiet"):
            extendUser.objects.filter(user=u).update(dietStatus=False)
            setDiet(foods, u, request)
            return redirect('/main')
            
        return output(foods, u, request)

def output(foods, u, request):
    e = extendUser.objects.get(user=u)
    foods =food.objects.all() 
    pro = 'Protein= '+str(e.reqProtein)
    carb = 'Carbohydrate= '+str(e.reqCarbs)
    fat = 'Fat= '+str(e.reqFat)
    cal = 'Calories = '+str(e.reqCalorie)
    macroStatus = e.macroStatus
    dietList=[]
    try:
        dietList = ast.literal_eval(str(e.diet))
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
    dietStatus = e.dietStatus
    dtStatus = e.dtStatus

    return render(request, "mainPage.html", {'dietList':dietList, 'pro':pro, 'carb':carb, 'fat':fat, 'cal':cal, 'macroStatus':macroStatus, 'foods':foods,  'dietStatus':dietStatus, 'dtStatus':dtStatus})

def setProgram(foods, u, request):
    if request.method == 'POST':
        age = int(request.POST['age'])
        height = int(request.POST['height'])
        weight = int(request.POST['weight'])
        goal = request.POST['goal']
        sex = request.POST['sex']
        activity = request.POST['activity']
        
        req = calcMacro(age, height, weight, goal, sex, activity)
        #print(age, height, weight, goal, sex, activity, req, '--------------------------------')
        try:
            e = extendUser.objects.get(user=u)#if extendUser exists
            print(e)
        except: #if extendUser doesnt exist then SAVE
            s= "Your current Macronutrients are: "
            user = extendUser(height=height, age=age, weight=weight, goal=goal, sex=sex, activity=activity, reqCalorie=req[0], reqProtein=req[1], reqCarbs=req[2], reqFat=req[3], user=u, macroStatus=s)
            user.save()
        else: #if no error given then UPDATE
            #status already updated
            dtStatus = "You have changed your program and the macro-nutrients have been re-assigned. Select foods again to create a new diet."
            s= "Your current Macronutrients are: "
            extendUser.objects.filter(user=u).update(height=height, age=age, weight=weight, goal=goal, sex=sex, activity=activity, reqCalorie=req[0], reqProtein=req[1], reqCarbs=req[2], reqFat=req[3], macroStatus=s, dtStatus=dtStatus, dietStatus=False)
        #return redirect('/main')
    return 0
    #return render(request, "mainPage.html", {'vis':1, 'pro':'Protein= '+str(req[1]), 'carb':'Carbohydrate= '+str(req[2]), 'fat':'Fat= '+str(req[3]),'cal':'Calories = '+str(req[0]), 'status':s, 'foods':foods, 'dtStatus'=s})

def setDiet(foods, u, request):
    e = extendUser.objects.get(user=u)
    s = ""
    cal = []
    p = []
    c = []
    f = []
    maxIntake = []
    Foods = request.POST.getlist('food')#get selected foods from multi-select
    
    for fo in Foods:
        F = food.objects.get(name = fo)
        #e.foods.add(F)#we need to remove all foods first before adding============================TO BE CHANGED
        cal.append(F.calorie)
        p.append(F.protein)
        c.append(F.carbohydrate)
        f.append(F.fat)
        maxIntake.append(F.maxIntake)
    
    maxCal = e.reqCalorie
    maxP = e.reqProtein
    maxC = e.reqCarbs
    maxF = e.reqFat
    items = len(Foods)
    count = [0]  # no. of calls
    maxItems = [0]
    Map = {}  # food : quantity
    Possibilities = {}  # count : Map  i.e all combinations
    macros = {}  # count : list  i.e each combination macros
    ans = {} #best possibilities(with max items)
    reqMacros = [maxCal, maxP, maxC, maxF]

    found=0
    calcPossibilities(items, maxCal, maxP, maxC, maxF, maxIntake, Map, reqMacros, Possibilities, macros, cal, p, c, f, Foods, count, maxItems, found)
    calcBest(Possibilities, macros, ans, maxItems)
        
    dietFoods = {}
    dietList = []
    
    for k in ans:
        dietFoods = ans[k]#taking the first possibility
        break
    #convert to string and set quantity
    if(dietFoods):#if possibility exists
        for k in dietFoods:
            fObj = food.objects.get(name=k)
            dietList.append([k, str(dietFoods[k]*fObj.quantity)+fObj.unit, str(round(fObj.protein*dietFoods[k],1)), str(round(fObj.carbohydrate*dietFoods[k],1)), str(round(fObj.fat*dietFoods[k],1)), str(round(fObj.calorie*dietFoods[k],1))])
        s+="Your current diet is displayed below. To change select foods again."
        extendUser.objects.filter(user=u).update(diet=str(dietList), dietStatus=True, dtStatus=s)
    else:
        s += "Add some more foods"
        extendUser.objects.filter(user=u).update(diet=str(dietList), dietStatus=False, dtStatus=s)
  
def calcMacro(age, height, weight, goal, sex, activity):
    reqCal = 0
    reqPro = 0
    reqCarb = 0
    reqFat = 0

    if(sex=='male'):
        reqCal=int((10*weight)+(6.25*height)-(5*age)+5)
    else:
        reqCal=int((10*weight)+(6.25*height)-(5*age)-161)

    if(activity == 'light'):
        reqCal = int(reqCal*1.2)
    elif(activity == 'moderate'):
        reqCal = int(reqCal*1.375)
    else:
        reqCal = int(reqCal*1.72)

    if(goal == 'fatloss'):
        reqPro = .4 * reqCal / 4
        reqCarb = .3 * reqCal / 4
        reqFat = .3 * reqCal / 9
    elif(goal == 'maintenance'):
        reqPro = .3 * reqCal / 4
        reqCarb = .4 * reqCal / 4
        reqFat = .3 * reqCal / 9
    else:
        reqPro = .3 * reqCal / 4
        reqCarb = .35 * reqCal / 4
        reqFat = .35 * reqCal / 9
    return [int(reqCal), int(reqPro), int(reqCarb), int(reqFat)]

def calcPossibilities(items, maxCal, maxP, maxC, maxF, maxIntake, Map, reqMacros, Possibilities, macros, cal, p, c, f, item, count, maxItems, found):
    if(found==1):
        sys.exit(0)
    if (maxCal < -50 or maxP < -15 or maxC < -20 or maxF < -10):
        return 0
    if (maxCal <= 0 or items <= 0):
        if ((maxP > -15 and maxP < 15) and (maxC > -20 and maxC < 20) and (maxF > -10 and maxF < 10) and (maxCal > -50 and maxCal < 50)):
            if(len(Map)==len(item)):
                found=1
            Possibilities[count[0]] = Map
            macros[count[0]] = [abs(maxP - reqMacros[1]), abs(maxC - reqMacros[2]), abs(maxF - reqMacros[3]),
                             abs(maxCal - reqMacros[0])]
            maxItems[0] = max(maxItems[0], len(Map))
            count[0]+=1
            return 0
        else:
            return -sys.maxsize

    if (cal[items - 1] > maxCal):
        return calcPossibilities(items - 1, maxCal, maxP, maxC, maxF, maxIntake.copy(), Map.copy(),reqMacros.copy(),Possibilities,macros,cal,p,c,f,item,count,maxItems,found)
    
    Excluding = calcPossibilities(items - 1, maxCal, maxP, maxC, maxF, maxIntake.copy(), Map.copy(),reqMacros.copy(),Possibilities,macros,cal,p,c,f,item,count,maxItems,found)
    if (maxIntake[items - 1] - 1 >= 0):
        maxIntake[items - 1] -= 1
        if (item[items - 1] in Map):
            Map[item[items - 1]] += 1
        else:
            Map[item[items - 1]] = 1
        Including = cal[items - 1] + calcPossibilities(items, maxCal - cal[items - 1], maxP - p[items - 1],
                                                       maxC - c[items - 1], maxF - f[items - 1], maxIntake.copy(), Map.copy(),
                                                        reqMacros.copy(), Possibilities, macros, cal, p, c, f, item, count, maxItems, found)
        Map[item[items - 1]] -= 1
        return max(Including, Excluding)
    return Excluding

def calcBest(Possibilities, macros, ans, maxItems):
    for x in Possibilities:
        if len(Possibilities[x])==maxItems[0]:
            ans[x]=Possibilities[x]