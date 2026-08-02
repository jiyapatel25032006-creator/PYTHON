# Reading Data//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales)

# Filtering Data//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales[sales ["Sales"] > 30000])

# Data Analysis
# Average sales://
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales["Sales"].mean())

# Reporting//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.groupby("Region")["Sales"].mean())


# head()//          Shows first 5 rows by default//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.head())

#                    Custom rows://
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.head(15))

# tail()//      # Shows last 5 rows by default.//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.tail())

                #Custom rows//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.tail(10))

# sample()//          # Returns random rows.//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.sample(10))

# shape//       Shows Rows × Columns//              NO BRACKET AFTER SHAPE
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.shape)

# columns//     Shows column names.//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.columns)

#index//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.index)

# dtypes//                  # Shows datatype of each column.//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.dtypes)

# info()//  # Very important function.//    #Rows # Columns# Datatypes # Missing values # Memory usage    
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.info())

# describe()//   # Statistical summary.//   #Includes:Mean Count Min Max Standard deviation
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.describe())

#  Selecting Data//                         Single Column//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales["Sales"])

                                            # Multiple columns//            TWO SQUARE BRACKETS
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales[["Sales","Region"]])

# Row Slicing//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales[0:15])

# Indexing in Pandas//   
#    loc[]               # Label based indexing.//          Particular rows for all columns
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.loc[0])

                        # Specific value://                 Particular row of particular columnm
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.loc[0,"Sales"])

# iloc[]            # Position based indexing.//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.iloc[0])


                        # Specific value://  
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.iloc[0,1])

# Basic Filtering             # Single Condition//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales[sales["Sales"] > 30000])

# Multiple Conditions//                 #AND(&)//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales[(sales["Sales"] > 30000) & (sales["Region"] == "East")])

                                        # OR (|)//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales[(sales["Sales"] > 30000) | (sales["Region"] == "East")])

# Sorting Data                                # sort_values()//
# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.sort_values( "Sales", ascending=True))

# import pandas as pd
# sales = pd.read_csv("sales_data_large.csv")
# print(sales.sort_index())










