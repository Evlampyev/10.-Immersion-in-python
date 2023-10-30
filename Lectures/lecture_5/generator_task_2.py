my_gen = (chr(i) for i in range(97, 123))
print(my_gen)  # <generator object <genexpr> at 0x000001ED58DD7D60>
for char in my_gen:
    print(char)


#Первый print даёт такой ответ, потому что my_gen - генератор, он не хранит значения
# они формируются по мере необходимости, при использовании генератора


