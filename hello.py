# vip message
message_vip = """
안녕하세요. {0}님, 파이썬 수업에 오신 걸 환영합니다.
오늘은 첫째날입니다. {0}님의 메일주소 {1}로 학습내용을 보내드립니다.
20% 특별 할인권을 보내드렸습니다. 
"""

# mail message 내용을 message 변수에 담는다. 
message = """
안녕하세요. {0}님, 파이썬 수업에 오신 걸 환영합니다.
오늘은 첫째날입니다. {0}님의 메일주소 {1}로 학습내용을 보내드립니다.
"""

# 보낼사람의 이름과 이메일주소를 입력을 받는다.
name = input("이름을 입력해 주세요.")
email = input("이메일을 입력해 주세요.")
vip = input("vip인가요? (y/n)")

# 메일 내용을 완성해서 출력한다.
if vip == 'y':
    complete = message_vip.format(name, email)
else:
    complete = message.format(name, email)

print(complete)
# send_email(complete, to=email)