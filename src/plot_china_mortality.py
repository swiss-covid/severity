import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fs=16

df = pd.read_csv('data/mortality.csv',skipinitialspace=True)

fig, axs = plt.subplots(1,2, figsize=(12,6))
age = 0.5*(df['age1']+df['age2'])
fig.suptitle("Severity in China Jan/Feb 2020 among confirmed cases", fontsize=1.3*fs)
axs[0].plot(age, df['case_fraction'], 'o-',  lw=3, label="Cases")
axs[0].plot(age, df['death_fraction'], 'o-', lw=3, label="Deaths")
axs[0].set_xticks(age, [f"{l}-{u}" for l,u in zip(df['age1'],df['age2'])])
axs[0].tick_params(labelsize=0.8*fs)
axs[0].set_ylabel('Distribution [%]', fontsize=fs)
axs[0].set_xlabel('Age', fontsize=fs)
axs[0].legend(fontsize=fs)

axs[1].plot(age, df['CFR'], 'o-', lw=3)
axs[1].set_xticks(age, [f"{l}-{u}" for l,u in zip(df['age1'],df['age2'])])
axs[1].set_ylabel('Case Fatality Ratio [%]', fontsize=fs)
axs[1].set_xlabel('Age', fontsize=fs)
axs[1].tick_params(labelsize=0.8*fs)


plt.savefig('../info/images/CFR.png')
