from Func.poly_func import polynomial
data = open('pol.txt', 'r')
my_list = [line.strip() for line in data]
pol_str = my_list[0].split()
res_pol = []
for i in range(len(pol_str)):
    if pol_str[i] != '+' and pol_str[i] != '0' and pol_str[i] != '=' :
        res_pol.append(pol_str[i])
print(res_pol)  # список из элементов 1ого многочлена

data1 = open('pol1.txt', 'r')
my_list_sec = [line.strip() for line in data1]
pol_str_sec = my_list_sec[0].split()
res_pol_sec = []
for i in range(len(pol_str_sec)):
    if pol_str_sec[i] != '+' and pol_str_sec[i] != '0' and pol_str_sec[i] != '=' :
        res_pol_sec.append(pol_str_sec[i])
print(res_pol_sec) # # список из элементов 2ого многочлена
