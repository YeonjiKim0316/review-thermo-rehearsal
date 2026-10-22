"""강사 제공 파일: 라우터가 분류기를 받는 의존성.

테스트에서는 `app.dependency_overrides[get_predict]` 로 가짜 함수로 바꿔 끼운다.
"""

from collections.abc import Callable

from app import sentiment


def get_predict() -> Callable[[list[str]], list[float]]:
    return sentiment.predict
