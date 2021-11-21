import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('StudentsPerformance.csv')
print(df.info())
df_f = df[df['gender']=='female']['lunch'].value_counts()
df_m = df[df['gender']=='male']['lunch'].value_counts()
standard_f = df_f['standard']
standard_m = df_m['standard']
free_reduced_f = df_f['free/reduced']
free_reduced_m = df_m['free/reduced']


print(standard_f, standard_m , free_reduced_f, free_reduced_m )
s = pd.Series(data = [standard_f,free_reduced_f,standard_m,free_reduced_m], index = ['F_s','F_f','M_s','M,f'])
s.plot(kind = 'pie')

plt.show()
