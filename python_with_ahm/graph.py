import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes=True)
tit=sns.load_dataset("titanic")
# print(tit)
p=sns.countplot(x="who",data=tit,hue="class")
p.set_title("statistic")
plt.show()