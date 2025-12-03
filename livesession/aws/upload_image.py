import boto3
import os

from botocore.exceptions import ClientError

session = boto3.Session(profile_name="ozbe15")
s3 = session.client("s3")

def upload_api():
    # 1. 사용자로부터 업로드 할 파일 경로를 입력
    file_path = input("업로드 할 파일 경로를 입력하세요: ").strip()

    # 2. 존재하는 파일인지 확인
    if not os.path.isfile(file_path):
        print("[error] 잘못된 파일 경로입니다.")
        return

    # 3. 파일 업로드 (boto3)
    try:
        s3.upload_file(file_path, "ozbe15-boto3-112233", file_path)
        print(f"[success] 새로운 파일 업로드: ozbe15-boto3-112233/{file_path}")
    except ClientError as e:
        print(f"[error] 파일 업로드를 실패했습니다: {e}")

if __name__ == "__main__":
    upload_api()
