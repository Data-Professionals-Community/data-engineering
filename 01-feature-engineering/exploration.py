# %%
import pandas as pd
from glob import glob
from sklearn import preprocessing
paths = glob(pathname='data/stata/*.dta')
from IPython.display import display

# %%
dfs = {
    p.split('/')[-1].split('_')[0]: pd.read_stata(p)
    for p
    in paths
}
for name, d in dfs.items():
    print(name)
    display(d)


# %%
dfa = dfs['Admin']

le = preprocessing.LabelEncoder()
le.fit(dfa['w1_questionnaire'])
dfa['w1_questionnaire_lebaled'] = le.transform(dfa['w1_questionnaire'])

dfa[['w1_questionnaire','w1_questionnaire_lebaled']].head(50)
# %%
