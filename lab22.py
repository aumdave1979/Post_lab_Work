import pandas as pd

def a():
    import pandas as pd 
 
    df = pd.read_csv(r"C:\Users\aumda\OneDrive\Desktop\clg_stuff\sem-3\python\data_sets_for_lab\data.csv")
    print("\nEach column:") 
    print(df.dtypes)

def b():
    import pandas as pd
    df = pd.read_csv(r"C:\Users\aumda\OneDrive\Desktop\clg_stuff\sem-3\python\data_sets_for_lab\data.csv")
    df["Number"] = df["Number"].fillna(df["Number"].mean())
    print("\nMissing values handled:\n")
    print(df)

b()