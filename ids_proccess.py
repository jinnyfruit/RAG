def read_input_ids_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            input_ids = file.read().splitlines()
        return input_ids, True, ""
    except Exception as e:
        return [], False, str(e)

# 파일 경로
file_path = 'clientNames.txt'

input_ids, success, error_message = read_input_ids_from_file(file_path)

# 결과 출력
if success:
    print("Input IDs loaded successfully.\n")
else:
    print(f"Error loading file: {error_message}")

if success:
    # 제외 아이디 리스트(풀무원TF팀, 코드클릭, 마음AI 계정)
    exclude_ids = ["sin8616", "hjjun0213", "yeajinyu", "case18", "sejookim", "hjjungl", 
                   "dmz2817", "heemis", "yspak82", "ananan", "zanghdnwls2", "tngyupp", "rhksgud123",
                   "jinnyfruit","st0304","chlwnsgh647","ellenalee","100bms",'mindslab','rhksgud1439']    

    # 제외된 아이디 리스트
    excluded_ids = []

    # 제외해야 할 아이디를 제외하고 중복 없이 출력할 고객 아이디 리스트 생성
    output_ids = []
    for id in input_ids:
        if id in exclude_ids:
            excluded_ids.append(id)
        else:
            output_ids.append(id)

    output_ids = list(set(output_ids))
    excluded_ids = list(set(excluded_ids))
    cnt = 0 

    print("\n======현황보고======\n")
    print("일자: 2024.01.16 오전 11시 50분")
    print("전체 인입건:", len(input_ids))
    print("실이용 고객수:", len(output_ids))
    print("제외된 아이디 수:", len(excluded_ids))

    print("\n===제외된 임직원ID===\n")
    for i in excluded_ids:
        print(i)

    print("\n===실이용 고객ID===\n")
    for i in output_ids:
        print(i)
