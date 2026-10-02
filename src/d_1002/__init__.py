# ① from .app import main
#    .app = 이 파일과 같은 폴더의 app.py  (점 1개 = 같은 폴더, 점 2개 .. = 한 단계 위 폴더)
#    import main = 그 파일 안의 main 함수를 가져온다
# ② __all__ = ["main"]
#    다른 곳에서 from 패키지 import * 로 가져갈 때, main만 딸려 가게 정하는 목록
#    (from 패키지 import 이름 처럼 이름을 직접 쓰면 __all__과 상관없이 가져올 수 있다)
# ③ 점(.) import는 패키지로 실행할 때만 동작한다. 파일을 직접 실행하면 ImportError
from .app import main

__all__ = ["main"]


# ---프로젝트 초기화---
print("프로젝트 초기화 init") 