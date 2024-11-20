from fastapi import APIRouter, HTTPException
from ..services.amazon_ads import (
    get_access_token, generate_report, check_report_status,
    download_report, process_report
)
from ..services.database import save_to_sql
from datetime import date, timedelta

router = APIRouter()


@router.get("/fetch-keywords")
def fetch_keywords():
    try:
        access_token = get_access_token()
        start_date = (date.today() - timedelta(days=3)).strftime('%Y-%m-%d')
        end_date = start_date

        report_id = generate_report(access_token, start_date, end_date)
        report_url = check_report_status(access_token, report_id)
        download_report(report_url)

        data = process_report()
        save_to_sql(data)
        return data.to_dict(orient='records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
