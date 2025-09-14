import pandas as pd

def load_study_pack(path="data/example_study_pack.csv"):
    return pd.read_csv(path)

def print_materials(df):
    for _, row in df.iterrows():
        print(f"[{row['id']}] {row['subject']} - {row['level']}\n{row['content']}\n")

if __name__ == "__main__":
    df = load_study_pack()
    print_materials(df)
