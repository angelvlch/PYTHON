# with open("task4.txt", "w") as f:
#     for i in range(5):
#         while True:
#             try:
#                 name = input("Enter name")
#                 if not name:
#                     print("Empty name!")
#                     continue
#                 form = input("Enter form")
#                 if not form:
#                     print("Empty form!")
#                     continue
#                 revenue = float(input("Enter revenue"))
#                 costs = float(input("Enter costs"))
#                 break
#             except(ValueError):
#                 print("Wrong value!\n")
#             except:
#                 print("Something is wrong!")
#             f.write(name + ' ')
#             f.write(form + ' ')
#             f.write(str(revenue) + ' ')
#             f.write(str(costs) + ' ')
import json

with open("task4.txt", "w") as file:
    file.write("firm_1 ooo 10600 5000\n")
    file.write("firm_2 3ao 14060 9000\n")
    file.write("firm_3 ip 15400 12000\n")

firm_data = []
with open("task4.txt", "r") as file:
    for line in file:
        parts = line.split()
        if len(parts) == 4:
            name, ownership, revenue, expenses = parts
            revenue, expenses = int(revenue), int(expenses)
            profit = revenue - expenses
            if profit >= 0:
                firm_data.append({name: profit})


total_profit = 0
num_firms_with_profit = 0
for firm in firm_data:
    a=list(firm.values())# key's value # []
    total_profit += a[0]
    num_firms_with_profit += 1

average_profit = total_profit / num_firms_with_profit

# l={}
# for firm in firm_data:
#     for name,profit in firm.items():
#         l[name]=profit

result_list = [{name: profit for firm in firm_data for name,profit in firm.items()}, {"average_profit": average_profit}]
print("res=",result_list)
with open("task4.json", "w") as json_file:
    json.dump(result_list, json_file, ensure_ascii=False, indent=4)
print("Done!")
