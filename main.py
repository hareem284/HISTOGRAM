import matplotlib.pyplot as plt

blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

psp=[blood_sugar_men,blood_sugar_women]
colors=['g','r']
lables=['men','woman']
binsa=[80,100,125,150,180,200]
plt.xlabel("blood sugar range")
plt.ylabel("total number of people")
plt.title("BLOOD SUGAR LEVEL CHART.")
plt.hist(psp,color=colors,label=lables,orientation='horizontal',bins=binsa,rwidth=2)
plt.show()