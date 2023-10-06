lst = [30, 75, 9, 97, 50, -4, 70, 59]
# q1
print(max(lst))
lst.remove(min(lst))
lst.sort()
print(lst[:4])
# q2
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python",1]]
count_mail_lst = sum(1 for sublist in main_lst if isinstance(sublist, list) and sublist[0] == "python")
print(count_mail_lst)
# q3
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
sentence = " ".join(word.capitalize() for word in my_lst)
print(sentence)
# q4
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
copied_lst = my_lst[:]
print(copied_lst)
# q5
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst[2], my_lst[4] = my_lst[4], my_lst[2]
print(my_lst)
# q6
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
sum_result = sum(nums)
print(sum_result)
# q7
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple1 = tuple1 + (9,)
print(tuple1)

# q8
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)

result_tuple = tuple1 + (9,) + tuple2
print(result_tuple)








