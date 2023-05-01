import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium 

'''
Comandos básicos de python
'''
#print
print("Hola, introduce tu nombre")
#input()
nombre = input()
print("Tu nombre es " + nombre)
#sum, max
nums = [4,2,6,2,1,9]
suma = sum(nums)
print(suma)
print(max(nums))
#numpy
a = np.array([1, 2, 3, 4, 5])
print(a)
lista = [3,6,1,7,86,232,4,1]
media = np.mean(lista)
print(media)
#matplotlib
x = ["A", "B", "C", "D", "E"]
y = [10, 5, 12, 8, 3]

#plt.bar(x, y)
#plt.scatter(x, y)
#plt.show()

#seaborn
'''
tips = sns.load_dataset("tips")
print(tips)
sns.lmplot(x="total_bill", y="tip", data=tips)
sns.barplot(x="day", y="total_bill", hue="sex", data=tips)
plt.show()
'''
#folium
'''
m = folium.Map( 
    location=[40.965, -5.664], 
    zoom_start=12, 
    tiles='Stamen Terrain' 
) 
tooltip = 'plaza Mayor'
folium.Marker([40.965, -5.664], popup='Plaza Mayor', tooltip=tooltip).add_to(m) 
m.save('map.html')
'''