df = pd.read_csv('crime_dataset_india.csv')
df.head()

city_names = df.City.value_counts().index

city_val = df.City.value_counts().values

#pie chart
plt.pie(city_val,labels= city_names)

#piechart for top 5 cities
plt.pie(city_val[:5],labels= city_names[:5], autopct = "%1.0f")

gender_counts = df["Victim Gender"].value_counts()

plt.bar(gender_counts.index, gender_counts.values, color="skyblue", edgecolor="black")
plt.title("Crimes by Gender")
plt.xlabel("Victim Gender")
plt.ylabel("Number of Crimes")
plt.show()

age_counts = df["Victim Age"].value_counts()
plt.bar(age_counts.index,age_counts.values, color = "Violet", edgecolor = "black")
plt.title("Number of crimes by Age")
plt.xlabel("age")
plt.ylabel("number of crime")
plt.show()

df2.to_csv("cleaned csv", index= False)
sns.distplot(df2['Victim Age'],kde = False)
plt.show()