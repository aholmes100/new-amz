import requests
import json
import time
import gzip
import pandas as pd
from datetime import date, timedelta
from ..utils.config import CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN, PROFILE_ID


def get_access_token():
    token_url = "https://api.amazon.com/auth/o2/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "refresh_token": REFRESH_TOKEN
    }
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        return response.json().get("access_token")
    else:
        raise Exception(f"Failed to obtain access token: {response.status_code} - {response.text}")


def generate_report(access_token, start_date, end_date):
    url = 'https://advertising-api.amazon.com/reporting/reports'
    headers = {
        'Content-Type': 'application/vnd.createasyncreportrequest.v3+json',
        'Amazon-Advertising-API-ClientId': CLIENT_ID,
        'Amazon-Advertising-API-Scope': PROFILE_ID,
        'Authorization': f'Bearer {access_token}'
    }

    data = {
        "name": f"Targeting Report for KWs {start_date}",
        "startDate": start_date,
        "endDate": end_date,
        "configuration": {
            "adProduct": "SPONSORED_PRODUCTS",
            "groupBy": ["targeting"],
            "columns": ["campaignName", "targeting", "cost", "clicks", "impressions", "campaignBudgetAmount",
                        "sales7d", "unitsSoldClicks7d", "purchases7d"],
            "reportTypeId": "spTargeting",
            "timeUnit": "SUMMARY",
            "format": "GZIP_JSON"
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json().get('reportId')
    else:
        raise Exception(f"Failed to request report: {response.status_code} - {response.text}")


def check_report_status(access_token, report_id):
    url = f'https://advertising-api.amazon.com/reporting/reports/{report_id}'
    headers = {
        'Amazon-Advertising-API-ClientId': CLIENT_ID,
        'Amazon-Advertising-API-Scope': PROFILE_ID,
        'Authorization': f'Bearer {access_token}'
    }

    while True:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            status = response.json().get('status')
            if status == 'COMPLETED':
                return response.json().get('url')
            elif status in ['IN_PROGRESS', 'PENDING', 'PROCESSING']:
                time.sleep(30)
            else:
                raise Exception(f"Unexpected report status: {status}")
        else:
            raise Exception(f"Failed to check report status: {response.status_code} - {response.text}")


def download_report(report_url):
    response = requests.get(report_url, stream=True)
    if response.status_code == 200:
        with open('report.json.gz', 'wb') as file:
            file.write(response.raw.read())
    else:
        raise Exception(f"Failed to download report: {response.status_code} - {response.text}")


def process_report():
    with gzip.open('report.json.gz', 'rb') as f:
        report_data = pd.read_json(f)
    return report_data
