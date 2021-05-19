import seaborn as sns
import matplotlib.pyplot as plt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")

plt.show()