# This Python file uses the following encoding: utf-8

# sql alchemy를 사용한 model 들을 db에 생성하는 역활을 하는 파일

from database import init_db


if __name__ == "__main__":
    print "init db start"
    init_db()