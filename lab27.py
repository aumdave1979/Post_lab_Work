import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def a():
    # initialise data of lists
    data = {'Name':[ 'Aum' , 'Viraj' , 'Vishant' , 'Om' ],
            'Age':[ 30 , 21 , 29 , 28 ]}
    df = pd.DataFrame( data )
    sns.boxplot( data['Age'] )
    plt.show()

def b():
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
data = {
    'Name': ['Aum', 'Niraj', 'Om', 'viraj'],
    'Age': [30, 21, 29, 28]
}
df = pd.DataFrame(data)
sns.violinplot(x=df['Age'])
plt.show()

b()
