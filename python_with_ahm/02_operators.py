#print(6/3)
# print(8//2)
# print(7//2)
# print(7/2)
# print(7%2)
# x=5
# x+=10
# print(x)
# a=input("what's your name?")
# print("my name is", a)
# x=int(input("what's your age ?"))
# # =18
# if x > 18 :
#     print("you are eligible")
# else:
#     print("you are now underage")
# end()
# food="biryani"
# print(food.find("y"))
# a="i love me,myself,i,mine"
# print(a.split(","))

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes=True)

titanic=sns.load_dataset("titanic")
sns.catplot(x="sex",y="survived",hue="class",kind="bar",data=titanic)
plt.show()