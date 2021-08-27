import pytest
from datetime import datetime
import pytz
from main import app


@pytest.fixture
def client():
  return app.test_client()

def test_status_code(client):
  r = client.get('/')
  assert(r.status_code == 200)

def test_current_time_in_msk(client):
  r = client.get('/')
  MSK = pytz.timezone('Europe/Moscow')
  current_time = datetime.now(MSK).strftime('%H:%M:%S')
  assert r.data.decode('utf-8') == current_time