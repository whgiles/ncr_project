```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data_path = "../data/MSA_Practicum_Data_v1.0/"
```

### Accounts
No missing values


```python
account_data = pd.read_csv(data_path + "accounts.csv", dtype=str)
print(f"shape: {account_data.shape}")
account_data.head()
```

    shape: (75252, 3)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>global_transaction_id</th>
      <th>ticket_num</th>
      <th>account_num_hash</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>000000000002</td>
      <td>2529</td>
      <td>07137282970344898644</td>
    </tr>
    <tr>
      <th>1</th>
      <td>000000000004</td>
      <td>2531</td>
      <td>01006825571181167519</td>
    </tr>
    <tr>
      <th>2</th>
      <td>000000000005</td>
      <td>2532</td>
      <td>04778982719252047857</td>
    </tr>
    <tr>
      <th>3</th>
      <td>000000000006</td>
      <td>2533</td>
      <td>01006825571181167519</td>
    </tr>
    <tr>
      <th>4</th>
      <td>000000000015</td>
      <td>2542</td>
      <td>13744291601319509904</td>
    </tr>
  </tbody>
</table>
</div>



### Transaction Data
No missing values


```python
transaction_data = pd.read_csv(data_path + "transactions.csv", dtype=str)
transaction_data['num_items'] = pd.to_numeric(transaction_data.num_items)
transaction_data['ticket_total_value'] = pd.to_numeric(transaction_data.ticket_total_value)
transaction_data['date'] = pd.to_datetime(transaction_data.date)
print(f"shape: {transaction_data.shape}")
transaction_data.head()
```

    shape: (124934, 8)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>global_transaction_id</th>
      <th>store_num</th>
      <th>ticket_num</th>
      <th>date</th>
      <th>transaction_start_time</th>
      <th>transaction_end_time</th>
      <th>num_items</th>
      <th>ticket_total_value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>000000000000</td>
      <td>000003</td>
      <td>2527</td>
      <td>2020-07-01</td>
      <td>07:03:30</td>
      <td>07:03:45</td>
      <td>4</td>
      <td>296</td>
    </tr>
    <tr>
      <th>1</th>
      <td>000000000001</td>
      <td>000003</td>
      <td>2528</td>
      <td>2020-07-01</td>
      <td>07:04:22</td>
      <td>07:04:35</td>
      <td>10</td>
      <td>300</td>
    </tr>
    <tr>
      <th>2</th>
      <td>000000000002</td>
      <td>000003</td>
      <td>2529</td>
      <td>2020-07-01</td>
      <td>07:04:55</td>
      <td>07:06:15</td>
      <td>2</td>
      <td>373</td>
    </tr>
    <tr>
      <th>3</th>
      <td>000000000003</td>
      <td>000003</td>
      <td>2530</td>
      <td>2020-07-01</td>
      <td>07:06:22</td>
      <td>07:06:46</td>
      <td>7</td>
      <td>862</td>
    </tr>
    <tr>
      <th>4</th>
      <td>000000000004</td>
      <td>000003</td>
      <td>2531</td>
      <td>2020-07-01</td>
      <td>07:08:13</td>
      <td>07:08:54</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### Items in Transaction
No missing values


```python
item_transaction_data = pd.read_csv(data_path + "items_transactions.csv", dtype=str)
item_transaction_data['dept_num'] = pd.to_numeric(item_transaction_data.dept_num)
item_transaction_data['qty_sold'] = pd.to_numeric(item_transaction_data.qty_sold)
item_transaction_data['item_price'] = pd.to_numeric(item_transaction_data.item_price)
item_transaction_data['qty_is_weight'] = pd.to_numeric(item_transaction_data.qty_is_weight)
item_transaction_data['date'] = pd.to_datetime(item_transaction_data.date)

print(f"shape: {item_transaction_data.shape}")

item_transaction_data.head()
```

    shape: (1293520, 9)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>global_transaction_id</th>
      <th>item_id</th>
      <th>dept_num</th>
      <th>qty_sold</th>
      <th>item_price</th>
      <th>qty_is_weight</th>
      <th>ticket_num</th>
      <th>date</th>
      <th>time_scanned</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>000000000000</td>
      <td>00000000004889</td>
      <td>6</td>
      <td>3</td>
      <td>99</td>
      <td>0</td>
      <td>2527</td>
      <td>2020-07-01</td>
      <td>07:03:30</td>
    </tr>
    <tr>
      <th>1</th>
      <td>000000000000</td>
      <td>00000000003125</td>
      <td>6</td>
      <td>460</td>
      <td>429</td>
      <td>1</td>
      <td>2527</td>
      <td>2020-07-01</td>
      <td>07:03:34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>000000000001</td>
      <td>00000000000005</td>
      <td>20</td>
      <td>4</td>
      <td>100</td>
      <td>0</td>
      <td>2528</td>
      <td>2020-07-01</td>
      <td>07:04:22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>000000000001</td>
      <td>00000000000002</td>
      <td>20</td>
      <td>6</td>
      <td>100</td>
      <td>0</td>
      <td>2528</td>
      <td>2020-07-01</td>
      <td>07:04:25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>000000000002</td>
      <td>00007013201045</td>
      <td>1</td>
      <td>1</td>
      <td>299</td>
      <td>0</td>
      <td>2529</td>
      <td>2020-07-01</td>
      <td>07:05:06</td>
    </tr>
  </tbody>
</table>
</div>



### Item Descriptions
36885 ecomm missing values
1516 unique catagories


```python
item_descriptions_data = pd.read_csv(data_path + "items_descriptions.csv", dtype=str)
print(f"shape: {item_descriptions_data.shape}")
item_descriptions_data.head()
```

    shape: (48551, 6)





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>item_id</th>
      <th>description</th>
      <th>ecomm_description</th>
      <th>category</th>
      <th>item_type</th>
      <th>upc</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>00000000000001</td>
      <td>PAN DULCE SENCILLO</td>
      <td>Mexican Sweet Bread/Pan Dulce Mexicano, 1 Count</td>
      <td>020101020</td>
      <td>0</td>
      <td>00000000000010</td>
    </tr>
    <tr>
      <th>1</th>
      <td>00000000000002</td>
      <td>BOLILLO FRENCH ROLLS</td>
      <td>Bolillo, French Rolls, 1 Count</td>
      <td>020101210</td>
      <td>0</td>
      <td>00000000000020</td>
    </tr>
    <tr>
      <th>2</th>
      <td>00000000000003</td>
      <td>BOLILLO QUESO/CHILE JALAP</td>
      <td>Jalapeño and Cheese Bolillo, 1 Count</td>
      <td>020101210</td>
      <td>0</td>
      <td>00000000000030</td>
    </tr>
    <tr>
      <th>3</th>
      <td>00000000000004</td>
      <td>EMPANADA</td>
      <td>NaN</td>
      <td>020101020</td>
      <td>0</td>
      <td>00000000000040</td>
    </tr>
    <tr>
      <th>4</th>
      <td>00000000000005</td>
      <td>MIni Bolillo</td>
      <td>BOLILLO SMALL, 2 OZ</td>
      <td>020101210</td>
      <td>0</td>
      <td>00000000000050</td>
    </tr>
  </tbody>
</table>
</div>




```python
len(item_descriptions_data.category.unique())
item_descriptions_data['item_type'].value_counts()

```




    0      44432
    30      2052
    12       640
    16       603
    14       391
    15       213
    101      141
    102       37
    31        18
    7         14
    8          9
    17         1
    Name: item_type, dtype: int64




```python
df = item_transaction_data[['qty_sold', 'item_price']].loc[item_transaction_data['qty_is_weight']==0]
df['revenue'] = df['qty_sold'] * df['item_price']

df.revenue.describe()
```




    count    941908.000000
    mean        298.895562
    std         445.707479
    min      -35078.000000
    25%          99.000000
    50%         199.000000
    75%         399.000000
    max       40000.000000
    Name: revenue, dtype: float64




```python

```


```python

```
