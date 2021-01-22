import time
import random
English_word_list = []
Korean_word_list = []

print("외우려는 단어들을 영어 단어와 한글 단어 순으로 저에게 알려주세요")

time.sleep(1)

test_start = False

while True:
    English_word = str(input("외우려는 영어 단어를 입력하세요. 외우려는 단어 입력 후 테스트를 시작하고 싶으시면 q 또는 start를 입력하세요!>> "))
    if English_word == "q" or English_word == "start":
        if not English_word_list or not Korean_word_list:
            print("외우려는 영어단어 혹은 한글 단어를 다시 입력해주세요")
            English_word = str(input("외우려는 영어 단어를 입력하세요.>> "))
        else:
            time.sleep(0.5)
            print("TEST 시작!!!")
            time.sleep(0.5)
            test_start = True
            break
    English_word_list.append(English_word)

    Korean_word = str(input("위에 입력한 영어단어의 한글 뜻을 입력하세요>> "))
    if Korean_word == "q" or Korean_word == "start":
        print("영어단어만 입력 하셨습니다. 입력한 영단어의 한글 뜻을 입력후 q를 다음에 입력하세요")
        Korean_word = str(input("위에 입력한 영어단어의 한글 뜻을 다시 입력하세요>> "))
    Korean_word_list.append(Korean_word)

if test_start == True:
    print("test가 시작됩니다!")
    time.sleep(1)
    for i in range(len(English_word_list)):
        random_word_list_number = random.randrange(len(Korean_word_list))
        answer_for_Korean = input(f"{English_word_list[random_word_list_number]}의 뜻>> ")
        if(answer_for_Korean == Korean_word_list[random_word_list_number]):
            print("정답입니다") 
            Korean_word_list.remove(Korean_word_list[random_word_list_number])
            English_word_list.remove(English_word_list[random_word_list_number])
            random_word_list_number = random.randrange(len(Korean_word_list))
        else:
            print("오답입니다")
            answer_for_Korean = input(f"{English_word_list[random_word_list_number]}의 뜻>> ")
            random_word_list_number = random.randrange(len(Korean_word_list))
    
# print(Korean_word, English_word)
print(English_word_list, Korean_word_list)