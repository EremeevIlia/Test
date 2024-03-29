Домашнее задание 1
1.1. Скачать данные kc-house-data
import pandas as pd

df = pd.read_csv('kc_house_data.csv', sep=',')
df.head()
id	date	price	bedrooms	bathrooms	sqft_living	sqft_lot	floors	waterfront	view	...	grade	sqft_above	sqft_basement	yr_built	yr_renovated	zipcode	lat	long	sqft_living15	sqft_lot15
0	7129300520	20141013T000000	221900.0	3	1.00	1180	5650	1.0	0	0	...	7	1180	0	1955	0	98178	47.5112	-122.257	1340	5650
1	6414100192	20141209T000000	538000.0	3	2.25	2570	7242	2.0	0	0	...	7	2170	400	1951	1991	98125	47.7210	-122.319	1690	7639
2	5631500400	20150225T000000	180000.0	2	1.00	770	10000	1.0	0	0	...	6	770	0	1933	0	98028	47.7379	-122.233	2720	8062
3	2487200875	20141209T000000	604000.0	4	3.00	1960	5000	1.0	0	0	...	7	1050	910	1965	0	98136	47.5208	-122.393	1360	5000
4	1954400510	20150218T000000	510000.0	3	2.00	1680	8080	1.0	0	0	...	8	1680	0	1987	0	98074	47.6168	-122.045	1800	7503
5 rows × 21 columns

1.2 Изучите стоимости недвижимости
import matplotlib.pyplot as plt
plt.hist(df['price'])
plt.title('Распределение стоимости')
plt.xlabel('price')
plt.ylabel('Количество')
Text(0, 0.5, 'Количество')

1.3 Изучите распределение квадратуры жилой площади
Постройте график
Назовите график
Сделайте именование оси x и оси y
Сделайте выводы
plt.hist(df['sqft_living'])
plt.title('Распределение жилой площади')
plt.xlabel('sqft_living')
plt.ylabel('Количество')
Text(0, 0.5, 'Количество')

1.4 Изучите распределение года постройки
Постройте график
Назовите график
Сделайте именование оси x и оси y
Сделайте выводы
plt.hist(df['yr_built'])
plt.title('Распределение года постройки')
plt.xlabel('yr_built')
plt.ylabel('Количество')
Text(0, 0.5, 'Количество')

Домашнее задание 2
2.1 Изучите распределение домов от наличия вида на набережную
Постройте график
Сделайте выводы
data = df['waterfront'].value_counts()
names = data.index
values = data.values

data
0    21450
1      163
Name: waterfront, dtype: int64
plt.pie(values, autopct = '%.1f%%', labels = names)
([<matplotlib.patches.Wedge at 0x7f7d35708ee0>,
  <matplotlib.patches.Wedge at 0x7f7d35714550>],
 [Text(-1.0996912625289312, 0.026060067488889404, '0'),
  Text(1.0996912610039797, -0.026060131839218025, '1')],
 [Text(-0.5998315977430533, 0.014214582266666945, '99.2%'),
  Text(0.5998315969112615, -0.014214617366846195, '0.8%')])

2.2 Изучите распределение этажей домов
Постройте график
Сделайте выводы
data = df['floors'].value_counts()
names = data.index
values = data.values

data
1.0    10680
2.0     8241
1.5     1910
3.0      613
2.5      161
3.5        8
Name: floors, dtype: int64
plt.pie(values, autopct = '%.1f%%', labels = names)
([<matplotlib.patches.Wedge at 0x7f7d357593d0>,
  <matplotlib.patches.Wedge at 0x7f7d35739df0>,
  <matplotlib.patches.Wedge at 0x7f7d357680d0>,
  <matplotlib.patches.Wedge at 0x7f7d357687f0>,
  <matplotlib.patches.Wedge at 0x7f7d35768f10>,
  <matplotlib.patches.Wedge at 0x7f7d35776670>],
 [Text(0.020225263915618102, 1.0998140473277942, '1.0'),
  Text(-0.43815513727130967, -1.0089698091037016, '2.0'),
  Text(0.9627084765709827, -0.5321582369355734, '1.5'),
  Text(1.0895069519517122, -0.1515737498674799, '3.0'),
  Text(1.0996359552126889, -0.02829780916391729, '2.5'),
  Text(1.0999992562786765, -0.0012791350042693163, '3.5')],
 [Text(0.011031962135791691, 0.5998985712697059, '49.4%'),
  Text(-0.23899371123889615, -0.5503471686020189, '38.1%'),
  Text(0.5251137144932632, -0.29026812923758544, '8.8%'),
  Text(0.5942765192463885, -0.0826765908368072, '2.8%'),
  Text(0.5998014301160121, -0.015435168634863975, '0.7%'),
  Text(0.5999995943338234, -0.0006977100023287179, '0.0%')])

2.3 Изучите распределение состояния домов
Постройте график
Сделайте выводы
data = df['condition'].value_counts()
names = data.index
values = data.values

data
3    14031
4     5679
5     1701
2      172
1       30
Name: condition, dtype: int64
plt.pie(values, autopct = '%.1f%%', labels = names)
([<matplotlib.patches.Wedge at 0x7f7d34b80f70>,
  <matplotlib.patches.Wedge at 0x7f7d34c86e50>,
  <matplotlib.patches.Wedge at 0x7f7d34c86a30>,
  <matplotlib.patches.Wedge at 0x7f7d321108e0>,
  <matplotlib.patches.Wedge at 0x7f7d358182b0>],
 [Text(-0.49690197886140847, 0.9813706860323558, '3'),
  Text(0.21000073456107682, -1.0797683508437392, '4'),
  Text(1.0489088894797076, -0.33134595451045795, '5'),
  Text(1.0993745907520605, -0.03708785796914586, '2'),
  Text(1.0999895419218622, -0.004796630330982164, '1')],
 [Text(-0.2710374430153137, 0.535293101472194, '64.9%'),
  Text(0.1145458552151328, -0.5889645550056759, '26.3%'),
  Text(0.572132121534386, -0.1807341570057043, '7.9%'),
  Text(0.5996588676829421, -0.020229740710443193, '0.8%'),
  Text(0.5999942955937428, -0.0026163438168993617, '0.1%')])

Домашнее задание 3
Исследуйте, какие характеристики недвижимости влияют на стоимость недвижимости, с применением не менее 5 диаграмм из урока.
Анализ сделайте в формате storytelling: дополнить каждый график письменными выводами и наблюдениями.
import numpy as np
corr_matrix = df.corr()
corr_matrix = np.round(corr_matrix, 1)
corr_matrix[np.abs(corr_matrix) < 0.3] = 0
corr_matrix
id	price	bedrooms	bathrooms	sqft_living	sqft_lot	floors	waterfront	view	condition	grade	sqft_above	sqft_basement	yr_built	yr_renovated	zipcode	lat	long	sqft_living15	sqft_lot15
id	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
price	0.0	1.0	0.3	0.5	0.7	0.0	0.3	0.3	0.4	0.0	0.7	0.6	0.3	0.0	0.0	0.0	0.3	0.0	0.6	0.0
bedrooms	0.0	0.3	1.0	0.5	0.6	0.0	0.0	0.0	0.0	0.0	0.4	0.5	0.3	0.0	0.0	0.0	0.0	0.0	0.4	0.0
bathrooms	0.0	0.5	0.5	1.0	0.8	0.0	0.5	0.0	0.0	0.0	0.7	0.7	0.3	0.5	0.0	0.0	0.0	0.0	0.6	0.0
sqft_living	0.0	0.7	0.6	0.8	1.0	0.0	0.4	0.0	0.3	0.0	0.8	0.9	0.4	0.3	0.0	0.0	0.0	0.0	0.8	0.0
sqft_lot	0.0	0.0	0.0	0.0	0.0	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.7
floors	0.0	0.3	0.0	0.5	0.4	0.0	1.0	0.0	0.0	-0.3	0.5	0.5	0.0	0.5	0.0	0.0	0.0	0.0	0.3	0.0
waterfront	0.0	0.3	0.0	0.0	0.0	0.0	0.0	1.0	0.4	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
view	0.0	0.4	0.0	0.0	0.3	0.0	0.0	0.4	1.0	0.0	0.3	0.0	0.3	0.0	0.0	0.0	0.0	0.0	0.3	0.0
condition	0.0	0.0	0.0	0.0	0.0	0.0	-0.3	0.0	0.0	1.0	0.0	0.0	0.0	-0.4	0.0	0.0	0.0	0.0	0.0	0.0
grade	0.0	0.7	0.4	0.7	0.8	0.0	0.5	0.0	0.3	0.0	1.0	0.8	0.0	0.4	0.0	0.0	0.0	0.0	0.7	0.0
sqft_above	0.0	0.6	0.5	0.7	0.9	0.0	0.5	0.0	0.0	0.0	0.8	1.0	0.0	0.4	0.0	-0.3	0.0	0.3	0.7	0.0
sqft_basement	0.0	0.3	0.3	0.3	0.4	0.0	0.0	0.0	0.3	0.0	0.0	0.0	1.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0
yr_built	0.0	0.0	0.0	0.5	0.3	0.0	0.5	0.0	0.0	-0.4	0.4	0.4	0.0	1.0	0.0	-0.3	0.0	0.4	0.3	0.0
yr_renovated	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	1.0	0.0	0.0	0.0	0.0	0.0
zipcode	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	-0.3	0.0	-0.3	0.0	1.0	0.3	-0.6	-0.3	0.0
lat	0.0	0.3	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.3	1.0	0.0	0.0	0.0
long	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.3	0.0	0.4	0.0	-0.6	0.0	1.0	0.3	0.3
sqft_living15	0.0	0.6	0.4	0.6	0.8	0.0	0.3	0.0	0.3	0.0	0.7	0.7	0.0	0.3	0.0	-0.3	0.0	0.3	1.0	0.0
sqft_lot15	0.0	0.0	0.0	0.0	0.0	0.7	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.0	0.3	0.0	1.0
import seaborn as sns
plt.figure(figsize = (10, 8))
sns.heatmap(corr_matrix, annot = True, linewidths = 5, cmap = 'coolwarm')
<AxesSubplot:>

sns.jointplot(x = df['sqft_living'], y = df['price'], kind = 'reg');

Чем больше площадь, тем больше стоимость

plt.figure(figsize = (16, 8))

sns.boxplot(x = df['price'], y = df['grade'].astype('str'), whis = 1.5)
            
plt.title('Распределение цены в зависимости от качества постройки и дизайна')
plt.xlabel('Цена')
plt.ylabel('Качество постройки и дизайна');

Из графика видно, что ящик 13 правее всех, в то время как ящики 1-7 находятся, примерно, на одном уровне слева. То есть, чем выше качество постройки и дизайна, тем выше стоимость дома.

plt.figure(figsize = (16, 8))

sns.boxplot(x = df['price'], y = df['view'].astype('str'), whis = 1.5)
            
plt.title('Распределение цены в зависимости от вида из окна')
plt.xlabel('Цена')
plt.ylabel('Вид из окна');

Вид из окна оценивается от 0 до 4. Ящик 4 находится правее остальных, ящик 0 - левее. То есть, чем лучше вид, тем выше стоимость.

plt.figure(figsize = (16, 8))

sns.boxplot(x = df['price'], y = df['condition'].astype('str'), whis = 1.5)
            
plt.title('Распределение цены в зависимости от состояния дома')
plt.xlabel('Цена')
plt.ylabel('Состояние дома');

Из графика следует, что чем лучше состояние дома, тем выше его цена.