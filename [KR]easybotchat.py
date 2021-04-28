# -*- coding: utf-8 -*- 
import time

print(" ")
print("제작자 크흠 버전-1.0.0")
time.sleep(0.5)
print("디스코드 봇 대화구문 만들기 귀찮을때 쓰는 기능.")
time.sleep(0.5)
print("무단 복제, 무단 배포 절대 불가")
time.sleep(0.5)
print(" ")

f = open("easybotchat.txt", 'w')
f.close()

user = 1
startmess = 0
imbed = 0
end = 0
message = 1

print("이 말은 최초 1회만 나옵니다. 잘 읽어주세요.")
print(" ")
time.sleep(0.5)
print("임베드로 넘어가길 원한다면 '임베드'라고 쳐주세요")
print(" ")
time.sleep(0.5)
print("임베드의 기본 색상은 초록입니다. 바꾸고 싶으시다면 님이 알아서 바꾸세요")
print(" ")
time.sleep(0.5)
print("끝내길 원한다면 '끝'이라고 쳐주세요")
print(" ")
time.sleep(0.5)
print("기본적으론 유저가 보낸 메시지의 전체가 명령어와 동일하면 작동합니다.")
print(" ")
time.sleep(0.5)
print("위의 기능을 원한다면 '기본메시지'라고 쳐주세요")
print(" ")
time.sleep(0.5)
print("시작하는 말이 유저의 명령어가 되고싶다면 '시작메시지'이라고 쳐주세요.")
print(" ")
time.sleep(0.5)


while 1:
    
    if imbed == (1): 
        while imbed == (1):
            print(" ")
            vinput = input(f"{user}번째 유저의 명령어를 입력해 주세요.(현재 임베드)")
            if vinput == ("기본메시지"):
                imbed = 0
                message = 1
                break

            elif vinput == ("시작메시지"):
                imbed = 0
                startmess = 1
                break

            elif vinput == ("끝"):
                imbed = 0
                end = 1
                break

            else:
                f = open("easybotchat.txt", 'a')
                f.write("\n   ")
                f.write("\n    elif message.content == (""'" + vinput + "'""):")
                f.close()
                print(" ")
                vinput2 = input("임베드의 제목을 적어주세요")
                print(" ")
                vinput = input(f"{vinput}에 대한 대답을 입력해 주세요")
                f = open("easybotchat.txt", 'a')
                f.write("\n      embed = discord.Embed(title=""'" + vinput2 + "'"", description=""'" + vinput + "'"", color=0x00ff00)")
                f.close()
                user = user + 1
                
        

    elif startmess == (1):
        while startmess == (1):
            print(" ")
            vinput = input(f"{user}번째 유저의 명령어를 입력해 주세요.(현재 시작메시지)")
            if vinput == ("기본메시지"):
                startmess = 0
                message = 1
                break

            elif vinput == ("임베드"):
                startmess = 0
                imbed = 1
                break

            elif vinput == ("끝"):
                startmess = 0
                end = 1
                break

            else:
                f = open("easybotchat.txt", 'a')
                f.write("\n   ")
                f.write("\n    elif message.content.startswith(""'" + vinput + "'""):")
                f.close()
                print(" ")
                vinput = input(f"{vinput}에 대한 대답을 입력해 주세요")
                f = open("easybotchat.txt", 'a')
                f.write("\n       await message.channel.send(""'" + vinput + "'"")")
                f.close()
                user = user + 1

    elif message == (1):
        while message == (1):
            print(" ")
            vinput = input(f"{user}번째 유저의 명령어를 입력해 주세요.(현재 기본 메시지)")
            if vinput == ("시작메시지"):
                message = 0
                startmess = 1
                break

            elif vinput == ("임베드"):
                message = 0
                imbed = 1
                break

            elif vinput == ("끝"):
                message = 0
                end = 1
                break

            else:
                f = open("easybotchat.txt", 'a')
                f.write("\n   ")
                f.write("\n    elif message.content == (""'" + vinput + "'""):")
                f.close()
                print(" ")
                vinput = input(f"{vinput}에 대한 대답을 입력해 주세요")
                f = open("easybotchat.txt", 'a')
                f.write("\n       await message.channel.send(""'" + vinput + "'"")")
                f.close()
                user = user + 1
    elif end == (1):
        break


print("모든 명령어가 입력되었습니다.")
time.sleep(1)
print("당신의 코드에 아래의 명령어들을 입력해주세요")
time.sleep(1)
f = open("easybotchat.txt", 'r')
data = f.read()
print(" ")
print(data)
print(" ")
close = input("창을 닫으려면 엔터키를 누르세요")