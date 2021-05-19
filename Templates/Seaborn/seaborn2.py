import seaborn as sns
import matplotlib.pyplot as plt
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

sns.set_theme(color_codes=True)

tips = sns.load_dataset("tips")

sns.regplot(x="total_bill", y="tip", data=tips);

plt.show()