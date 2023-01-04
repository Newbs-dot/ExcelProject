import gspread
from oauth2client.service_account import ServiceAccountCredentials

credentials = {
    "type": "service_account",
    "project_id": "excel-bot-369907",
    "private_key_id": "9c896d41da52aed9eddc6320c4ac6be0b33f7686",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCvlvPITE66mp4/\nsqNt9XKgVHE7F+VZO5Kk0V0UjD4iYgq/CDgGkJZb/1pytIGx8j/W82/Z/EDdobxH\nEq6bM4maD+euPzHGtrB3gsSdkG7DSzqwdxJcOjQpWtROzmKeczXysz6Xxu4ri1C+\n0YjdFkv+mSImxrhavIFLbJ3DZ4uRSOfmBjgs6jxKcminLq/kSK7ND2ndNDriGI1J\nEvCWUpp+Hxa/RLo4LTdisgCwxSCrRk28iPOiyT+3AMyokthbtaPXWpIw0Wf/UFv9\n08+cXLRbm1IILD3IxRIaLBecmpZxmsp5vNFsZmOL3tIJUy3HM5eYDtuMEFjAYdNq\nB9D7qlpjAgMBAAECggEANLue5w6TrlL1J6gckM9f52q0vsyEYnITrk/6Jkuf9W+A\nTrLHMKGHpoVfwocXVDuulH1zoAGz8Vu7UZT4vz+RGaWhLKFp74W6JYouRiu0OA6F\nx61a5DvOooTWsfwlffSXxRWzvJ1PteAXFdeTxOIHXKTcrsyLXSSzp9Us5Bxau/yr\nm0PWNnDmNXSDm43gyR0Z9mz6et/y5uaGeLPi5zLM2Wl/uy4ykUhRLMNdYXbh1fBb\ngAGY7RsNaMBliZJ5bnlBDreg6j1W86vzDbFJDpx8aviwGHDzTPURQ9B0kuGWI93x\nk/tGUd59YC+qBGfP0BcaBB0M5IV3BDTW9XUfrr+28QKBgQDiL4JaMMInZpi/irM2\nDyJMEMZuJ1CuYiWr7zpR2erhMmJCOkaY/ud+ESG8lpDTlqZUwcLKzT3zt3TkWY7e\n+uhzszpMrEv5aA18/jRDhaMWd3qAKgZtwEaB8pQWawDE9ziq+9qh4srIJtq0D0W1\nZDUuZlQO9bQONfiX6gnh6NmfNwKBgQDGvB2Cpcbi4yNyiKdUmB+br3lh/3nOburT\nAGF08ait34Q1q+j1PdAwPSLF2PVvbxJcm2TUl8m/tZeixlBWSVQMehDtpTeOyFZR\n4RrXjjzQ6S+83C7eZNaDIuo6iVESJ69WsY++n6F+8/KHfLH6P3kq9DGQcw4tpNEW\n8my8r9C8NQKBgDjc8MxzzZvSMzyURhGlJF4zKW+v+pycmBPthJ/nRSFwZTt5Ix57\nlv8el3it8aMAELjmLW6Gwrhuurhdu4lbUu0jddioyEDfY+S0k7cV9bZEO0vVROB6\noj8xGQG5zOu3q0txHbntJkXDXuA9pqy/kI8lsqRAKRAZiXHHqMxembdpAoGAOUqP\nw1MhI9VRKbqFapi0PAB5IKwypDVLkuqALeNgukc+aO6XKOPZ+Z4WQS0LjEVb6MCP\nb84WRiMGhNFg5Y8cIMCr0qaXfpz4bYBUaaHCnIMs1OgwxsIRKRrOpXNioLY6EOb9\nRnnkZ6HR4Actk7PqrVxaUYcppjTmZhQbDsYsiaUCgYAAgJnjvPZm3Wy8eyx+iKU/\n/e++cYqMi4IQYk96q9xm8W3N6YDsV+JXFX7TqqYZo3frYk3sAK6v5c5FKnmxB3Jz\nXVkx2CcMou3jDC3U/4G5pjfAQFJAB3iQvpfcI4jsqkBfeSk1cLM33JV+KQR4yIC7\nCAAC70A6lsjjnzxjs26qFQ==\n-----END PRIVATE KEY-----\n",
    "client_email": "excel-telegram-bot@excel-bot-369907.iam.gserviceaccount.com",
    "client_id": "115387746598316254796",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/excel-telegram-bot%40excel-bot-369907.iam.gserviceaccount.com"
}


def gspread_read(url,month):
    account_credentials = ServiceAccountCredentials.from_json_keyfile_dict(
        credentials,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    client = gspread.authorize(account_credentials)
    table = client.open_by_url(url)
    ws = table.worksheet(month)

    return ws
