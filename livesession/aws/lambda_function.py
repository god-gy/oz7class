import json
import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):
    # 1. HTTP 요청 (requests)
    response = requests.get('https://example.com')

    # 2. html -> bs4 파싱 (bs4)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 3. bs4 객체에서 데이터 추출
    h1_tags = []
    for tag in soup.find_all('h1'):
        h1_tags.append(tag.text)

    return {
        'statusCode': 200,
        'body': json.dumps(h1_tags)
    }

# 파일 압축 방법
# 1. 압축 희망 파일로 경로 이동
# cd pa*
# 2. 상위 폴더에 압축파일 생성
# zip -r ../packages.zip .
# 3. 상위 폴더로 이동
# cd ..

# 압축한 폴더에 파일 추가하는 방법
# zip packages.zip lambda_function.py