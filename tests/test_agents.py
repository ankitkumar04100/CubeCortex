import pytest
from src.agents.anomaly_detection import detect_anomaly

def test_anomaly_detection():
    data = [1, 2, 1, 100]  # contains anomaly
    assert detect_anomaly(data) == True
