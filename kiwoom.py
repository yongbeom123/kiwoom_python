import requests

# API 요청을 위한 기본 정보
api_key = 'YOUR_API_KEY'
base_url = 'https://api.kiwoom.com'
version = 'v1'

# 종목 코드 조회 API 예시
def get_stock_codes():
    endpoint = f'{base_url}/{version}/stock/codes'
    headers = {'Authorization': f'Bearer {api_key}'}

    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code} - {response.text}')
        return None

# 다른 API 함수들도 비슷하게 작성 가능

if __name__ == '__main__':
    # 종목 코드 조회 API 호출
    stock_codes = get_stock_codes()

    if stock_codes:
        # 종목 코드 조회 결과 출력
        for stock in stock_codes:
            print(f"종목 코드: {stock['code']}, 종목 이름: {stock['name']}")

