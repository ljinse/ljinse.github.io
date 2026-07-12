import json
from datetime import datetime, timezone
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent / "data.json"


def crawl() -> dict:
    # TODO: 실제 크롤링 로직으로 교체 (예: requests로 페이지 요청 후 파싱)
    now = datetime.now(timezone.utc).isoformat()
    return {"updatedAt": now}


def main() -> None:
    data = crawl()
    DATA_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
