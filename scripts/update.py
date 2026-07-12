import json
from datetime import datetime, timezone
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.json"


def fetch_data() -> dict:
    # TODO: 크롤링 로직 준비되면 이 함수 내용을 교체.
    # 지금은 임시로 이 Action이 실행된 시각만 기록한다.
    now = datetime.now(timezone.utc).isoformat()
    return {"updatedAt": now}


def main() -> None:
    data = fetch_data()
    DATA_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
