import googletrans

trans = googletrans.Translator()  #구글 변역 객체 생성
result1 = trans.translate("뭐를 해볼까요? 중국어?", dest="en")
# print(googletrans.LANGUAGES) ->번역 언어의 dest에 삽입할 약자 찾기

print(result1.text)

result2 = trans.translate("뭐를 해볼까요? 중국어?", dest="ja")

result3 = trans.translate("뭐를 해볼까요? 중국어?", dest="zh-cn")

print(result1.text)
print(result2.text)
print(result3.text)