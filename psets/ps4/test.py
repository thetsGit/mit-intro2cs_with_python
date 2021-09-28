import string
# 
# for string in lis:
# for char in string:
#     for i in range(len(char)):
#     list(char).insert(i,'a')
# c ['c']
# bc['bc','cb']
# abc['abc','bac','bca','acb','cab','cba']


# def insert(lis,letter):
#         res = []
#         current_lis = []
#         for string in lis:
#             for i in range(len(string)+1):
#               current_lis = list(string)
#               current_lis.insert(i,letter)
#               res.append(''.join(current_lis))
#               current_lis = []
#         return res
# def get_permutations (sequence):
#     if (len(sequence) == 1):
#         return [sequence]
#     return insert(get_permutations(sequence[1:]),sequence[:1])
# print(get_permutations('dabc'))

# print(insert(['c'],'b'))
# print(insert(['bc', 'cb'],'a'))
# print(insert(['abc', 'bac', 'bca', 'acb', 'cab', 'cba'],'d'))
# insert([Sequence[0:-1]],Sequence[:-2:-1])
# # lis = list('blabla')
# # lis.insert(0,'a')
# # print(lis)
# print('apple'[:-1],'apple'[:-2:-1])


# print(string.ascii_lowercase)
# index = lowcase_letts.index('r')
# print(lowcase_letts[index+2 if (index + 2 < 26) else index + 2 - 26])
# dic = {}
# dic['b'] = dic.get('b',2)
# dic['c'] = dic.get('c',3)
# print(dic)