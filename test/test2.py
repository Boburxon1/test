def str_to_dict(lst):
    result = {}
    try:
        # 2 qadamdan yurib chiqamiz: [0]-key, [1]-value, keyin [2]-key, [3]-value ...
        for i in range(0, len(lst), 2):
            result[lst[i]] = lst[i+1]
    except IndexError:
        print("Xatolik: ro'yxat elementlari juft bo‘lishi kerak!")
    return result


# Test
print(str_to_dict(["1", "one", "2", "two", "3", "three", "4", "four"]))

print(str_to_dict(["dog", "bark", "cat", "meow", "cow", "moo"]))

