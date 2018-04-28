import pandas
df1=pandas.DataFrame([[1,2,3],[4,5,6]],columns=["first no","second no","third no"],index=[1,2])
df2=pandas.DataFrame([{"name":"pra"},{"name":"nshu"}],index=[1,2])
print(df2)
print(df1)
print(df1.mean())