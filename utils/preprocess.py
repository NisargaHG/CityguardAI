import pandas as pd

df = pd.read_csv("data/events.csv")

df["priority"] = df["priority"].fillna("Low")

df["zone"] = df["zone"].fillna("Unknown")

df["junction"] = df["junction"].fillna("Unknown")

df.to_csv("data/cleaned.csv", index=False)

print("Done") 