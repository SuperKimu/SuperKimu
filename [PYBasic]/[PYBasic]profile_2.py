def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("名前 : {0}\t年齢 : {1}\t".format(name, age), end= " ") #, end= " "で行を開けない、同じ行にする
    print(lang1, lang2, lang3, lang4, lang5)

profile("baby", 20, "chinese", "japanese", "english", "spanish", "russian")
#出力：名前 : baby     年齢 : 20        chinese japanese english spanish russian
profile("bbabbi", 21, "chinese", "japanese", " ", " ", " ")
#出力：名前 : bbabbi   年齢 : 21        chinese japanese      


def profile(name, age, *language): #＊を使い、可変引数活用可能
    print("名前 : {0}\t年齢 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("apple", 20, "chinese", "japanese", "english", "spanish", "russian")
profile("banana", 25, "chinese", "japanese")