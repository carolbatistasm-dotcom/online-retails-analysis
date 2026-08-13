# %%
import pandas as pd

df = pd.read_excel("online_retail.xlsx")
df.head(10)

# %%
# criar uma coluna com o valor total de cada item da transação
df["line_total"] = df["Quantity"] * df["UnitPrice"]
df.head(10)

# %%
# verificar valores ausentes por coluna
df.isna().sum()

# %%
# conferir quantas linhas serão removidas pelos valores ausentes
shape_before_na = df.shape

df = df.dropna()

shape_after_na = df.shape

print("Antes:", shape_before_na)
print("Depois:", shape_after_na)

# %%
# verificar quantidade de linhas completamente duplicadas
df.duplicated().sum()

# %%
# visualizar todas as ocorrências dos grupos duplicados
duplicates = df[df.duplicated(keep=False)]

duplicates.sort_values(
    by=[
        "InvoiceNo",
        "StockCode",
        "Description",
        "Quantity",
        "InvoiceDate",
        "UnitPrice",
        "CustomerID",
        "Country"
    ]
).head(30)

# %%
# remover apenas linhas completamente duplicadas
shape_before_duplicates = df.shape

df = df.drop_duplicates()

shape_after_duplicates = df.shape

print("Antes:", shape_before_duplicates)
print("Depois:", shape_after_duplicates)

# %%
# confirmar que não restaram duplicatas completas
df.duplicated().sum()

# %%
# verificas se existem linhas com quantidade negativa
df[df["Quantity"] < 0].shape
# %%
negatives = df[df["Quantity"] < 0]
negatives[["InvoiceNo", "Description", "Quantity", "UnitPrice"]].head(20)
# %%
# transações que começam com C são cancelamentos
negatives["InvoiceNo"].value_counts().head(20)

# %%
df["is_cancelled"] = df["InvoiceNo"].astype(str).str.startswith("C")
df.head(10)
# %%
#percentual de cancelamento
percent_cancelled = df["is_cancelled"].mean() * 100
print(f"Percentual de cancelamento: {percent_cancelled:.2f}%")

# %%
#Qual é o impacto financeiro desses cancelamentos?
df["line_total"].where(df["is_cancelled"]).sum()

# %%
# Qual é o impacto financeiro dos cancelamentos em relação ao faturamento total?
total_revenue = df["line_total"].sum()
total_revenue

# %%
cancelled_revenue = df["line_total"].where(df["is_cancelled"]).sum()
cancelled_revenue

#%%
# Percentual de faturamento cancelado
percent_cancelled_revenue = (cancelled_revenue / total_revenue) * 100
print(f"Percentual de faturamento cancelado: {percent_cancelled_revenue:.2f}%")


