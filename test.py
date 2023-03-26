#coding:cp1251

#from random import randint as RN 

#def GetRAndomList(n):
#    my_list = []
#    for i in range(n):
#        my_list.append(RN(0,100))
#    return my_list         

#def GetShuffleList(my_list):
#    shuf_list = []
#    while len(my_list) > 0:
#        index = RN(0,len(my_list)-1)
#        shuf_list.append(my_list[index])
#        my_list.pop(index)
#        print(len(my_list))
#    print(shuf_list)      

#original_list = GetRAndomList(10)
#GetShuffleList(original_list)

#from random import randint as RN

#def Get_Dict_koeff(k):
#    dict_koef = {}
#    for i in range(k, -1, -1):
#        dict_koef[i] = RN(-2,2)
#        if dict_koef[k] == 0:
#            dict_koef[k] = RN(-2,2)
#    return dict_koef

#def Get_polynomial(my_dict):
#    polynomial = ''

#    for i in range(len(my_dict)-1,-1,-1):
#        while i >=2:
#            if my_dict.get(i) < 0:                                                                      # ���������� ��������� � �������������� ��������������
#                if my_dict.get(i) != 0:                                                                 # ������� ����� � �������������� = 0
#                    if my_dict.get(i) !=-1:                                                             # �������� ��� ���������� � ������ ���������� ������������� = 1
#                        polynomial = polynomial + ' ' + str(my_dict.get(i)) + '*x**' +  str(i)
#                    else:
#                        polynomial = polynomial + ' - x**' +  str(i)
#            else:                                                                                       # ���������� ��������� � �������������� ��������������
#                if my_dict.get(i) != 0:
#                    if my_dict.get(i) !=1:    
#                        polynomial = polynomial + ' + ' + str(my_dict.get(i)) + '*x**' + str(i)  
#                    else:
#                        polynomial = polynomial + ' + ' 'x**' + str(i)
#        polynomial = polynomial + '?'
#    #print (polynomial)                    
#    if polynomial.startswith(' +'):                                                                 # ������� '+' � ������ ����������
#        polynomial = polynomial[2:]
    
#    print(polynomial)





    # if polynomial[-5] !=' ':
    #     polynomial = polynomial[:-5]
    # else:
       
    #     polynomial = polynomial[:-5] + ' 1'                                                           # ������ ��������� '*�**'
    # print(polynomial)
    # polynomial += ' = 0 '

#    return polynomial

#        # print(my_dict.get((i),'������ ����� ���'))
#        # print()
#        # print(my_dict.values(my_dict[i]))
   
    
#k = int(input('������� ��������� �������:'))
#print()
#my_dict = Get_Dict_koeff(k)
#print(my_dict)
#print()

#polynomial = Get_polynomial(my_dict)
#print(polynomial)
#print()

my_string = input('Введите число: ')
my_list = my_string.split()
print(my_list)

for index, item in enumerate(my_list):
    for i in range(len(item)-2):
        if item[i:i+3] == '���':
            my_list.remove(item)
            break
print(my_list)
new_string = ' '.join(my_list)
        
print(new_string)







