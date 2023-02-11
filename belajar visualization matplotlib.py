#!/usr/bin/env python
# coding: utf-8

# In[118]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[119]:


import matplotlib.pyplot as plt
import numpy as np


# In[120]:


#membuat sebuah figure dan axes

#data
x = [2, 5, 6, 9]
y = [3, 1, 5, 7]

fig, ax = plt.subplots()
ax.plot(x, y)


# In[121]:


#melakukan ploting tanpa membuat sebuah figure dan axes
x = [2, 5, 6, 9]
y = [3, 1, 5, 7]

plt.plot(x, y)


# In[122]:


#beberapa cara membuat figure dan axes
fig = plt.figure() #figure tanpa axes
fig, ax = plt.subplots() #membuat figure dan axes
fig, axs = plt.subplots(2, 3) #membuat sebuah figure dengan 2 baris axes dan 3 kolom axes


# In[123]:


#melakukan ploting dengan metode object oriented style

x = np.linspace(0, 2, 100) #membuat sebuah numerik yang dimulai dari 0 dan di akhiri sampai 2 dengan 100 angka

fig, ax = plt.subplots()

ax.plot(x, x, label = 'linear')
ax.plot(x, x**2, label = 'quadrat')
ax.plot(x, x**3, label = 'cubic')

ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title('simple ploting')
ax.legend()


# In[124]:


#melakukan ploting dengan metode ploting plt/ tanpa membuat figure dan axes

x = np.linspace(0, 3, 100)

plt.plot(x, x, label = 'linear')
plt.plot(x, x**2, label = 'quadrat')
plt.plot(x, x**3, label = 'cubic')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('simple ploting')
plt.legend()


# In[125]:


#membuat plotting sederhana
plt.plot([1, 3, 6, 8, 5])
plt.ylabel('y label')
plt.show()


# In[126]:


plt.plot([1, 3, 6, 8, 5], [2, 5, 7, 8, 9]) #array pertama mewakili x, array kedua mewakili y
plt.xlabel('x label')
plt.ylabel('y label')
plt.show()


# In[127]:


#pengaturan format pada plot 
plt.plot([1, 3, 6, 8, 5], [2, 5, 7, 8, 9], 'b--')
plt.axis([0, 8, 0, 10]) #plt.axis sebagai penanda seberapa besar dan kecil label x dan y
plt.show()


# In[128]:


x = np.arange(0., 7., 0.2)
x


# In[129]:


plt.plot(x, x, 'b--')
plt.plot(x, x**2, 'ys')
plt.plot(x, x**3, 'g-')
plt.show()


# In[130]:


plt.plot(x, x, 'b--',
        x, x**2, 'ys',
        x, x**3, 'g-')

plt.show()


# In[131]:


#plotting dengan keywords
data = {
    'a': np.arange(50),
    'c': np.random.randint(0, 50, 50),
    'd': np.random.rand(50)
}

data['b'] = data['a'] + 10 * np.random.rand(50)
data['d'] = np.abs(data['d']) * 100
data


# In[132]:


plt.scatter('a', 'b', data=data)
plt.xlabel('x label')
plt.ylabel('y label')
plt.show()


# In[133]:


plt.scatter('a', 'b', c='c', s='d', data=data) #c pada dimensi ketiga mewakili color, s pada dimensi keempat mewakili size
plt.xlabel('x label')
plt.ylabel('y label')
plt.show()


# In[134]:


#plotting untuk tipe data categorical
names = ['sample a', 'sample b', 'sample c', 'sample d']
value = [2, 4, 7, 9]

plt.plot(names, value, 'b--')
plt.show()


# In[135]:


plt.scatter(names, value)
plt.show()


# In[136]:


plt.bar(names, value)
plt.show()


# In[137]:


#simple line plot
x = np.arange(0.0, 2.0, 0.01)
x


# In[138]:


x1 = np.sin(2 * np.pi * x)
x1


# In[139]:


#simple plot line dengan metode object oriented style
fig, ax = plt.subplots()

ax.plot(x, x1, 'b--')
ax.set(xlabel='nilai x',
       ylabel='nilai cos x',
       title='visualisasi nilai sin x')
ax.grid()

plt.show()


# In[140]:


#simple plot line dengan metode pyplot style
plt.plot(x, x1, 'b--')
plt.xlabel('nilai x')
plt.ylabel('nilai cos x')
plt.title('visualisasi nilai sin x')
plt.grid()

plt.show()


# In[141]:


x1 = np.linspace(0.0, 5.0, 100)
x2 = np.linspace(0.0, 6.0, 100)
x1


# In[142]:


y1 = np.cos(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)
y1


# In[143]:


#multiple subplots sederhana dengan metode object oriented style
fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('visualisasi nilai cos $x_1$ dan $x_2$')

ax1.plot(x1, y1, 'b--')
ax1.set_ylabel('nilai cos $x_1$')
ax1.grid()

ax2.plot(x2, y2, 'ys-')
ax2.set_ylabel('nilai cos $x_2$')
ax2.set_xlabel('nilai sumbu x')
ax2.grid()

plt.show()


# In[144]:


#multiple subplots sederhana dengan metode pyplot style
plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'b--')
plt.title('visualisasi nilai cos $x_1$ dan $x_2$')
plt.ylabel('nilai cos $x_1$')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'ys-')
plt.ylabel('nilai cos $x_2$')
plt.xlabel('nilai sumbu x')
plt.grid()

plt.show()


# In[145]:


#membuat histogram
mu, sigma = 100, 15 #mean sebesar 100, dan standard deviation sebesar 15
x = mu + sigma * np.random.randn(10000)
x


# In[146]:


x.shape


# In[147]:


#membuat histogram sederhana dengan metode pyplot
plt.hist(x,
         bins=100,
         facecolor='b',
         alpha=0.25)

plt.xlabel('nilai sumbu x')
plt.ylabel('nilai sumbu y')
plt.title('histogram sederhana')

plt.grid()
plt.text(50, 300, '$\mu=100, \ \sigma=15$')

plt.show()


# In[148]:


#membuat histogram sederhana dengan metode object oriented style
fig, ax = plt.subplots()

ax.hist(x,
        bins=100,
        facecolor='y',
        alpha=0.25)

ax.set_xlabel('nilai sumbu x')
ax.set_ylabel('nilai sumbu y')
ax.set_title('histogram sederhana')

ax.grid()
ax.text(50, 300, '$\mu=100, \ \sigma=15$')

plt.show()


# In[149]:


#membuat barplot / barchart sederhana
data = [24, 57, 44, 80, 36, 92]
kategorik = ['A', 'B', 'C', 'D', 'E', 'F']


# In[152]:


plt.bar(kategorik, data)
plt.grid()

plt.xlabel('data kategorik')
plt.ylabel('data y')
plt.title('barplot sederhana')

plt.show()


# In[153]:


fig, ax = plt.subplots()

ax.bar(kategorik, data)
ax.grid()

ax.set_xlabel('data kategorik')
ax.set_ylabel('data y')
ax.set_title('barplot sederhana')

plt.show()


# In[155]:


#pengaturan grid dan color

plt.bar(kategorik,
        data,
        color='b',
        alpha=0.25)

plt.grid(linestyle='--',
         linewidth=1,
         axis='y',
         alpha=0.50)

plt.xlabel('data kategorik')
plt.ylabel('data y')
plt.title('barplot sederhana')

plt.show()


# In[156]:


fig, ax = plt.subplots()

ax.bar(kategorik,
       data,
       color='y',
       alpha=0.25)

ax.grid(linestyle='--',
        linewidth=1,
        axis='y',
        alpha=0.50)

ax.set(xlabel='data kategorik',
       ylabel='data y',
       title='baplot sederhana')

plt.show()


# In[158]:


#horizontal barplot dengan metode pyplot style
plt.barh(kategorik, data)

plt.grid(linestyle='--',
         linewidth=1,
         axis='y',
         alpha=0.25)

plt.xlabel('data y')
plt.ylabel('data kategorik')
plt.title('barplot sederhana')

plt.show()


# In[160]:


plt.barh(kategorik[::-1],
         data[::-1],
         color='b',
         alpha=0.25)

plt.grid(linestyle='--',
         linewidth=1,
         axis='y',
         alpha=0.50)

plt.xlabel('data y')
plt.ylabel('data kategorik')
plt.title('barplot sederhana')

plt.show()


# In[161]:


#horizontal barplot dengan metode object oriented style
fig, ax = plt.subplots()

ax.barh(kategorik[::-1],
        data[::-1],
        color='y',
        alpha=0.25)

ax.grid(linestyle='--',
        linewidth=1,
        axis='y',
        alpha=0.50)

ax.set(xlabel='data y',
       ylabel='data kategorik',
       title='barplot sederhana')

plt.show()


# In[167]:


#stacked barplot
data1 = [75, 33, 56, 79, 90, 21]
data2 = [90, 33, 52, 44, 67, 11]
kategorik = ['A', 'B', 'C', 'D', 'E', 'F']
x = np.arange(len(kategorik))
x


# In[168]:


#stacked barplot dengan metode pyplot
plt.bar(kategorik, data1, label='Data 1')
plt.bar(kategorik, data2, label='Data 2', bottom = data1)


plt.legend()

plt.grid(linestyle='--',
         linewidth=1,
         axis='y',
         alpha=0.50)

plt.xlabel('sumbu data kategorik')
plt.ylabel('data y')
plt.title('stacked barplot sederhana')

plt.show()


# In[169]:


plt.bar(kategorik,
        data1,
        label='Data 1',
        color='b',
        alpha=0.25)

plt.bar(kategorik,
        data2,
        label='Data 2',
        color='r',
        alpha=0.25,
        bottom = data1)

plt.legend()

plt.grid(linestyle='--',
         linewidth=1,
         axis='y',
         alpha=0.50)

plt.xlabel('sumbu data kategorik')
plt.ylabel('data y')
plt.title('stacked barplot sederhana')

plt.show()


# In[171]:


#stacked barplot sederhana dengan metode object oriented style
fig, ax = plt.subplots()

ax.bar(kategorik, data1, label='Data 1')
ax.bar(kategorik, data2, label='Data 2', bottom=data1)

ax.legend()

ax.grid(linestyle='--',
        linewidth=1,
        axis='y',
        alpha=0.50)

ax.set(xlabel='sumbu data kategorik',
       ylabel='data y',
       title='stacked barplot sederhana')

plt.show()


# In[172]:


fig, ax = plt.subplots()

ax.bar(kategorik,
       data1,
       label='Data 1',
       color='b',
       alpha=0.25)

ax.bar(kategorik,
       data2,
       label='Data 2',
       color='r',
       alpha=0.25,
       bottom=data1)

ax.legend()

ax.grid(linestyle='--',
        linewidth=1,
        axis='y',
        alpha=0.50)

ax.set(xlabel='sumbu data kategorik',
       ylabel='data y',
       title='stacked barplot sederhana')

plt.show()


# In[182]:


#grouped barplot
width = 0.35

plt.bar(x-width/2, data1, width, label='Data 1')
plt.bar(x+width/2, data2, width, label='Data 2')

plt.legend()

plt.xticks(x, kategorik)

plt.grid(linestyle='--',
         linewidth=1,
         axis='y',
         alpha=0.50)

plt.xlabel('sumbu data kategorik')
plt.ylabel('data y')
plt.title('grouped barplot sederhana')

plt.show()


# In[181]:


width = 0.35

plt.bar(x-width/2,
        data1,
        width,
        label='Data 1',
        color='b',
        alpha=0.25)

plt.bar(x+width/2,
        data2,
        width,
        label='Data 2',
        color='r',
        alpha=0.25)

plt.legend()

plt.xticks(x, kategorik)

plt.grid(linestyle='--',
         linewidth=1,
         axis='y',
         alpha=0.50)

plt.xlabel('sumbu data kategorik')
plt.ylabel('data y')
plt.title('grouped barplot sederhana')

plt.show()


# In[187]:


width = 0.35

fig, ax = plt.subplots()

ax.bar(x-width/2, data1, width, label='Data 1', color='y', alpha=0.25)
ax.bar(x+width/2, data2, width, label='Data 2', color='r', alpha=0.25)

ax.legend()

ax.set_xticks(x, kategorik)

ax.grid(linestyle='--',
        linewidth=1,
        axis='y',
        alpha=0.50)

ax.set(xlabel='sumbu data kategorik',
       ylabel='data y',
       title='grouped barplot sederhana')

plt.show()


# In[225]:


#membuat piechart sederhana

kategorik = ['A', 'B', 'C', 'D', 'E']
data = [110, 340, 220, 760, 550]


# In[226]:


plt.pie(data,
        labels=kategorik,
        autopct='%1.1f%%',
        startangle=90)

plt.title('piechart sederhana')

plt.show()


# In[228]:


fig, ax = plt.subplots()

ax.pie(data,
       labels=kategorik,
       autopct='%1.1f%%',
       startangle=90)

ax.set_title('piechart sederhana')

plt.show()


# In[229]:


#variasi warna piechart dengan data kategorik
warna = ['yellow', 'red', 'cyan', 'skyblue', 'purple']


# In[230]:


plt.pie(data,
        labels=kategorik,
        colors=warna,
        autopct='%1.1f%%',
        startangle=90)

plt.title('piechart dengan variasi warna')

plt.show()


# In[231]:


fig, ax = plt.subplots()

ax.pie(data,
       labels=kategorik,
       colors=warna,
       autopct='%1.1f%%',
       startangle=90)

ax.set_title('piechart dengan vaiasi warna')

plt.show()


# In[232]:


#variasi piechart dengan menambahkan explode pada variable data
explode_var = [0.0, 0.04, 0.02, 0.08, 0.06]


# In[233]:


plt.pie(data,
        labels=kategorik,
        explode=explode_var,
        autopct='%1.1f%%',
        colors=warna,
        startangle=50)

plt.title('piechart dengan variasi explode')

plt.show()


# In[234]:


fig, ax = plt.subplots()

ax.pie(data,
       labels=kategorik,
       explode=explode_var,
       colors=warna,
       autopct='%1.1f%%',
       startangle=50)

ax.set_title('piechart dengan variasi explode')

plt.show()


# In[243]:


data_ujian = [
    ['bejo', 70],
    ['tejo', 90],
    ['rika', 100],
    ['ajeng', 80],
    ['majid', 30]
]


# In[245]:


#membuat tableplot dengan metode object oriented style
fig, ax = plt.subplots()

table = plt.table(cellText=data_ujian,
                  loc='center')

table.set_fontsize(14)
table.scale(1, 3)

ax.axis(False)

plt.show()


# In[246]:


#membuat tableplot dengan metode pyplot style
table = plt.table(cellText=data_ujian,
                  loc='center')

table.set_fontsize(14)
table.scale(1, 3)

ax = plt.gca()
ax.axis(False)

plt.show

