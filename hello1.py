message = """
안녕하세요. {0}님, 파이썬 수업에 오신 걸 환영합니다.
오늘은 첫째날입니다. {0}님의 메일주소 {1}로 학습내용을 보내드립니다.
"""

while True:
    # 보낼사람의 이름과 이메일주소를 입력을 받는다.
    name = input("이름을 입력해 주세요.")
    email = input("이메일을 입력해 주세요.")

    # 메일 내용을 완성해서 출력한다.
    complete = message.format(name, email)
    print(complete) 

    end = input("종료할까요? (y/n)")
    if end == 'y':
        break

print("프로그램을 종료합니다.")