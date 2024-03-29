import googletrans
#
# trans = googletrans.Translator()  #구글 변역 객체 생성
# result1 = trans.translate("뭐를 해볼까요? 중국어?", dest="en")
# # print(googletrans.LANGUAGES) ->번역 언어의 dest에 삽입할 약자 찾기
#
# print(result1.text)
#
# result2 = trans.translate("뭐를 해볼까요? 중국어?", dest="ja")
#
# result3 = trans.translate("뭐를 해볼까요? 중국어?", dest="zh-cn")
#
# print(result1.text)
# print(result2.text)
# print(result3.text)


while True:
    korStr = input("번역할 문장을 입력하세요:")
    if korStr =="끝":
        break
    trans = googletrans.Translator()  #구글 변역 객체 생성
    result1 = trans.translate(korStr, dest="en")
    # print(googletrans.LANGUAGES) ->번역 언어의 dest에 삽입할 약자 찾기

    # print(result1.text)

    result2 = trans.translate(korStr, dest="ja")

    result3 = trans.translate(korStr, dest="zh-cn")

    print(f"입력하신 [{korStr}]는 영어로 [{result1.text}]입니다")
    print(f"입력하신 [{korStr}]는 일본어로 [{result2.text}]입니다")
    print(f"입력하신 [{korStr}]는 중국어로 [{result3.text}]입니다")
