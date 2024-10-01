import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

data = pd.read_csv('data.csv')
res_id = data['Responder_id']
languages  = data['LanguagesWorkedWith']


# We can use 2 Method to seperate language and grab the top 10 or 15 languages.
# one method is basic python programming and the second is builtin function from collections module

splitLanguage = languages.str.split(";") # We can't split directly because this is a series object
# so we have to use the str method to convet it into string and then call the split method
mycount = {}             # is used for counting the frequency
for lst in splitLanguage:  # splitlanguage has many list and each list has different languages
    for lan in lst:
        if  lan in mycount.keys():
            mycount[lan] += 1
        else:
            mycount[lan] = 1

# Now to grab the top 10 we need to to use sorted dictionary  and then sort by values

sortLanguage = sorted(mycount.items(), key = lambda  item: item[1],reverse= True)[:15]

# Now we need to seperate the language and counts of languages for plotting purpose

popularity = []
languagesLab = []
for lan in sortLanguage:
    popularity.append(lan[1])
    languagesLab.append(lan[0])

# To plot them on a bar char we need to use plt.bar
languagesLab.reverse()
popularity.reverse()               #it wil show the popular language at the top instead of bottom
color = ['r','c','y','m','k','b','g','pink','grey','orange','m','k','b','g','r']
barlabel = plt.barh(languagesLab,popularity,height=0.5,color= color)
plt.tight_layout()
plt.xlabel("Popularity",labelpad=10,color = 'red')
plt.ylabel("Languages",labelpad=10,size = 20,color = 'g')
plt.title("Languages Vs Popularity")
plt.bar_label(barlabel,labels = popularity)
# plt.xscale("log")        # To convert x-axis to log
# plt.yscale("log")        #  To convert y-axis to log
plt.show()










# Method 2:: using Counter from collection module

languageCounter  = Counter()            # it takes a list as an argument

for lists in splitLanguage:
    languageCounter.update(lists)
top_15 = languageCounter.most_common(15)


lan = []
pop = []
for tuple in top_15:
    lan.append(tuple[0])
    pop.append(tuple[1])

# plotting
barplot = plt.barh(lan,pop)
plt.bar_label(barplot,labels = pop,color = 'r',rotation = 0)
plt.title('Not reversed that why high lan is at bottom')
plt.show()


#To plot top 5 languages on the pie chart we have
top5_lang = lan[0:5]
top5_pop = pop[0:5]
plt.pie(top5_pop,labels= top5_lang,startangle=90,autopct="%1.1f%%",wedgeprops={'ls':'--','lw':4,'ec':'w'})
plt.title("Pie chart of top 5 languages")
plt.show()
