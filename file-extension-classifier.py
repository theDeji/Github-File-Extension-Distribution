import os 
import glob
import collections
import matplotlib.pyplot as plt

language = []
value = []

dirpath = r"/Users/bisiajiboye/Desktop/Dejii/reactApps/connect-all/src"
os.chdir(dirpath)
extension_dict = collections.Counter()
for filename in glob.glob("*"):
    name, ext = os.path.splitext(filename)
    extension_dict[ext] += 1

newList = list(sorted(extension_dict.items()))

for tuplee in newList:
    language.append(tuplee[0])
    value.append(tuplee[1])

print(language)
print(value)

fig = plt.figure("Language Distribution")
ax = fig.add_axes([0,0,1,1])
ax.pie(value, labels=language, autopct=str)
plt.show()