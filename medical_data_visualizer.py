import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

    

# 1
df = pd.read_csv(
    'medical_examination.csv',
    index_col='id'
    )

# 2
BMI=df['weight']/((df['height']/100)**2)
df['overweight'] = BMI.apply(lambda x: 1 if x>25 else 0)

# 3
df['gluc']=df['gluc'].apply(lambda x: 1 if x>1 else 0)
df['cholesterol']=df['cholesterol'].apply(lambda x: 1 if x>1 else 0)

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars='cardio',value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])
    df_cat['total']=0
    variable_list=['cholesterol','gluc','smoke','alco','active','overweight']
    for variables in variable_list:
        for cardio in range(2):
            for variable_val in range(2):
                df_cat.loc[((df_cat['cardio']==cardio) & (df_cat['variable']==variables) & (df_cat['value']==variable_val)),"total"]=df_cat[(df_cat['cardio']==cardio) & (df_cat['variable']==variables) & (df_cat['value']==variable_val)].shape[0]


    # 6
    df_cat = df_cat.drop_duplicates()
    

    # 7



    # 8
    fig = sns.catplot(data=df_cat,x='variable',y='total',col='cardio',hue='value',kind='bar')
    fig=fig.figure

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo']<=df['ap_hi'])&
        (df['height']>=df['height'].quantile(0.025))&
        (df['height']<=df['height'].quantile(0.975))&
        (df['weight']>=df['weight'].quantile(0.025))&
        (df['weight']<=df['weight'].quantile(0.975))
    ]
    df_heat.reset_index(inplace=True)
    # 12
    corr = df_heat.corr()

    # 13
    mask = corr.where(~(np.triu(np.ones(corr.shape)).astype(bool)))



    # 14
    fig, ax = plt.subplots(figsize=(12,6))

    # 15
    sns.heatmap(data=mask,annot=True,fmt=".1f",center=0,vmax=0.3,linewidths=0.5,square=True,ax=ax,cbar_kws={'shrink':0.5})



    # 16
    fig.savefig('heatmap.png')
    return fig
