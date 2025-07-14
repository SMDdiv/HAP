import pandas as pd

def main():
    
    df = pd.read_csv("data.csv")
    print("=================================")
    print(" Dataset Summary ")
    print("=================================")
    print(df.info())
    print("=================================")
    print("\n First 10 Records ")
    print("=================================")
    print(df.head(10))
    print("=================================")
    print("\n Missing Values Check")
    print(df.isnull().sum())
    print("=================================")
    print("\n Summary Statistics")
    print(df.describe(include='all'))
    print("=================================")

if __name__ == "__main__":
    main()
