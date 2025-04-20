# 53
# l = ['','','a']
# print( any(l))


# p54
# import webbrowser
# l = [5,5,5,1]
# if all(l):
#     webbrowser.open('k4.gif')
#
# else:
#     print('😎')
#


# p55
# խնդիրը լուծած կա գրքում դրա համար չեմ գրել



# p56

# l = [2,4,4,5]
# k =  list(map(lambda x:x%2==0,l))
# if all(k):
#     print('հրաշալի է')
# else:
#     print('Գրողը տանի')



# p57
# import webbrowser
# l = [-1,5,4,2,-8,-6]
# k = list(map(lambda x:x>0,l))
# if any(k):
#     webbrowser.open('k2.mp4')
# else:
#     print(False)

#p58
# import  os
# l = ['A','B','Gen AI']
# k = list(map(lambda x:x=='Gen AI',l))
# if any(k):
#     print('Շնորհավորում ենք')
# else:
#     os.system("shutdown /s /t 0")

# p59
# from gtts import gTTS
#
#
# l = ['Armenia','door',]
# k = list(map(lambda x: x[0]=='A',l))
# if all(k):
#     text = "Yes"
#     g = gTTS(text=text, lang='en')
#     g.save("output.mp3")
# else:
#     text = "No"
#     g = gTTS(text=text, lang='en')
#     g.save("output.mp3")

# #60
# l = [8,9,10,7]
# k = [l[i]<l[i+1] for i in range(len(l)-1)]
# if any(k):
#     print('👌')
# else:
#     print('🤨')



# 61
# import webbrowser
# l = ['Aram','m','Polar']
# k = list(map(lambda x:len(x)>3,l))
# if all(k):
#     webbrowser.open('m.gif')
#
# else:
#     webbrowser.open('k.mp4')





