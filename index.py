# import matplotlib.pyplot as plt
# plt.plot([1,2,3], [10,20,30])
# plt.show()

# import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [10,20,30,40,50]
# plt.plot(x, y)
# plt.show()

# Real World Example: Monthly Sales-------------------------------------
# import matplotlib.pyplot as plt
# months = [1,2,3,4,5]
# sales = [10000,15000,18000,25000,30000]
# plt.plot(months, sales)
# plt.grid()
# plt.title("Monthly Sales Report")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.show()

# Student Marks----------------------------------------------------------------------

# import matplotlib.pyplot as plt

# subjects = [1,2,3,4,5]
# marks = [55,60,72,85,90]

# plt.plot(subjects, marks)
# plt.grid()
# plt.title("Student Vs marks")
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.show()

# Multiple Line Plot-------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# months = [1,2,3,4]
# sales_2024 = [100,200,300,400]
# sales_2025 = [150,250,350,500]
# plt.plot(months, sales_2024)
# plt.plot(months, sales_2025)
# plt.grid()
# plt.show()

#  Adding Labels for Multiple Lines-----------------------------------------------
# import matplotlib.pyplot as plt

# months = [1,2,3,4]

# sales_2024 = [100,200,300,400]
# sales_2025 = [150,250,350,500]

# plt.plot(months, sales_2024, label="2024 year")
# plt.plot(months, sales_2025, label="2025 year")
# plt.title("2024 and 2025 Sales Trend")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.legend()

# plt.show()

# Real Business Example--------------------------
# import matplotlib.pyplot as plt

# months = ["Jan","Feb","Mar","Apr"]

# amazon_sales = [20000,30000,35000,45000]

# plt.plot(months, amazon_sales)

# plt.title("Amazon Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Revenue")
# plt.grid()

# plt.show()

# Practice Questions-----------------------------------------------------------------------------
# Beginner Level------------------------
# 1. Create line chart for:
# import matplotlib.pyplot as plt
# marks = [50,60,70,80,90]
# subjects=[1,2,3,4,5]

# plt.plot(subjects,marks)
# plt.title("Student vs Subjects")
# plt.xlabel("subjects")
# plt.ylabel("marks")
# plt.grid()
# plt.show()

# 2. Create graph for temperature.
# import matplotlib.pyplot as plt
# temp = [32,34,35,38,40]
# city=["ahmedabad","gandhinagar","mumbai","baroda","surat"]

# plt.plot(city,temp)
# plt.title("temp vs city")
# plt.xlabel("city")
# plt.ylabel("temp")
# plt.grid()
# plt.show()

# 3. Create graph for expenses.
# import matplotlib.pyplot as plt
# expense = [5000,6000,7000,8000]
# income=[30000,12000,9000,5000]
# plt.plot(expense,income)
# plt.title("income vs expense")
# plt.xlabel("expense")
# plt.ylabel("income")
# plt.grid()
# plt.show()

# Intermediate Level------------------------------------------------------
# 4. Create multiple line graph for:------------------------
# 2024 sales and 2025 sales.-------------------------------
# import matplotlib.pyplot as plt

# months = [1,2,3,4]

# sales_2024 = [100,200,300,400]
# sales_2025 = [150,250,350,500]

# plt.plot(months, sales_2024, label="2024 year")
# plt.plot(months, sales_2025, label="2025 year")
# plt.title("2024 and 2025 Sales Trend")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.legend()

# plt.show()

# Assignment-----------------------------------------------------------------------------------------------------
# Task 1        # Create Student Marks Visualization.
# 1. Create line chart for:
# import matplotlib.pyplot as plt
# marks = [50,60,70,80,90]
# subjects=[1,2,3,4,5]

# plt.plot(subjects,marks)
# plt.title("Student vs Subjects")
# plt.xlabel("subjects")
# plt.ylabel("marks")
# plt.grid()
# plt.show()

# Task 2        # Create Company Revenue Trend.----------------------------------------------------------
# import matplotlib.pyplot as plt
# months = [1,2,3,4,5,6,7,8,9,10,11,12]
# sales = [10000,15000,18000,25000,30000,40000,20000,50000,45000,35000,12000,12500]
# plt.plot(months, sales)
# plt.grid()
# plt.title("Monthly Sales Report")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.show()




































