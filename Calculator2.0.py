from asyncio.windows_events import NULL


input_string = input("Enter elements of a list separated by space: ")
var_list = input_string.split()
print("list: ", var_list)

for i in range(len(var_list)):
    var_list[i] = int(var_list[i])

print("\n")
print("Remember 1 les action than elements:", len(var_list), "elements!")
input_string = input("Enter action of a list separated by space: ")
act_list = input_string.split()

print(var_list[0], act_list[0], var_list[1])
