import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
%matplotlib inline
plt.style.use("fivethirtyeight")

df = pd.read_csv('/Users/edwardt/Desktop/Bb_reports/Tools_usage1.csv')
df = df.sort_values(by=['DISTINCT_TOOL_COURSE_ACCESSED'],ascending=False)
rows = df.iloc[7:69]
# df.head(70)
rows = rows[['NAME','DISTINCT_TOOL_COURSE_ACCESSED','TOOL_ACCESSES','DISTINCT_TOOL_USERS','TOOL_HOURS']]
filter = rows['NAME'].str.contains("bb|label") 
Bb_tools = rows[filter]
Bb_tools['NAME']= Bb_tools['NAME'].apply(lambda x: x.split('.')[0])

tech_tools = rows[~filter]
tech_tools.loc[60,"NAME"] = "Atomic Learning"
tech_tools.loc[37,"NAME"] = "Partner Cloud"
tech_tools.loc[45,"NAME"] = "WIKI"
tech_tools.loc[15,"NAME"] = "Collborate Ultra"


Updated_list = tech_tools.drop([42,7,45,62])

import seaborn as sns
# sns.set_theme(style="white")
sns.relplot(x="DISTINCT_TOOL_USERS",y="DISTINCT_TOOL_COURSE_ACCESSED",hue="NAME", size="TOOL_ACCESSES", sizes=(40,400), alpha=.7, palette="muted",
            height=6,data=Updated_list)
plt.title("Tool Usage")
plt.xlabel('Students')
plt.ylabel('Courses')
plt.savefig('/Users/edwardt/Desktop/Bb_reports/tools2.png')
plt.show()



