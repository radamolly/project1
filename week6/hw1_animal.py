import pandas as pd

data = pd.read_csv('animal.csv')

df = pd.DataFrame(data)

print(df.groupby('Animal')['Weight'].mean())

print(df.loc[df['Age'].max()]['Animal'])
print(df.loc[df['Age'].min()]['Animal'])

cat_have_vaccine = df.loc[(df['Vaccinated'] == True) & (df['Animal'] == 'Cat'), 'Animal']
all_cat = df.loc[(df['Animal'] == 'Cat')]
vc2 = len(cat_have_vaccine)
vc3 = len(all_cat)
percent_cat = ((vc2 / vc3)*100)
print("cat = ", int(percent_cat),"%")

dog_have_vaccine = df.loc[(df['Vaccinated'] == True) & (df['Animal'] == 'Dog'), 'Animal']
all_dog = df.loc[(df['Animal'] == 'Dog')]
vc4 = len(dog_have_vaccine)
vc5 = len(all_dog)
percent_dog = ((vc4 / vc5)*100)
print("dog = ", int(percent_dog),"%")

rabbit_have_vaccine = df.loc[(df['Vaccinated'] == True) & (df['Animal'] == 'Rabbit'), 'Animal']
all_rabbit = df.loc[(df['Animal'] == 'Rabbit')]
vc6 = len(rabbit_have_vaccine)
vc7 = len(all_rabbit)
percent_rabbit = ((vc6 / vc7)*100)
print("rabbit = ", int(percent_rabbit),"%")

fish_have_vaccine = df.loc[(df['Vaccinated'] == True) & (df['Animal'] == 'Fish'), 'Animal']
all_fish = df.loc[(df['Animal'] == 'Fish')]
vc8 = len(fish_have_vaccine)
vc9 = len(all_fish)
percent_fish = ((vc8 / vc9)*100)
print("fish = ", int(percent_fish),"%")

bird_have_vaccine = df.loc[(df['Vaccinated'] == True) & (df['Animal'] == 'Bird'), 'Animal']
all_bird = df.loc[(df['Animal'] == 'Bird')]
vc10 = len(bird_have_vaccine)
vc11 = len(all_bird)
percent_bird = ((vc10 / vc11)*100)
print("bird = ", int(percent_bird),"%")

age_max = (df.groupby('Animal')['Age'].max())
weight_max = (df.groupby('Animal')['Weight'].max())
all_max = age_max + weight_max
print(all_max)