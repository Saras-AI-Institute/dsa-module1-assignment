import pytest
from log_engine import LoglyticsEngine

def test_task1_parsing():
    engine = LoglyticsEngine()
    raw = "  12:00:00 | CRITICAL | user_99 | System Crash  "
    parsed = engine.parse_and_archive_log(raw)
    
    assert isinstance(parsed, tuple), "Parsed log must be a tuple"
    assert parsed == ("12:00:00", "CRITICAL", "user_99", "System Crash")
    assert len(engine.logs_archive) == 1

def test_task2_unique_users():
    engine = LoglyticsEngine()
    engine.register_user("user_1")
    engine.register_user("user_2")
    engine.register_user("user_1") # Duplicate
    
    assert engine.get_unique_user_count() == 2

def test_task3_error_mapping():
    engine = LoglyticsEngine()
    engine.track_error_frequency("ERROR", "Timeout")
    engine.track_error_frequency("ERROR", "Timeout")
    engine.track_error_frequency("INFO", "User logged in") # Should be ignored
    engine.track_error_frequency("CRITICAL", "Auth failure")
    
    assert engine.error_counts.get("Timeout") == 2
    assert engine.error_counts.get("Auth failure") == 1
    assert "User logged in" not in engine.error_counts

def test_task4_priority_queue():
    engine = LoglyticsEngine()
    
    log_w = ("10am", "WARNING", "u1", "Low disk")
    log_e = ("11am", "ERROR", "u2", "DB fail")
    log_c = ("12pm", "CRITICAL", "u3", "Core melt")
    log_i = ("01pm", "INFO", "u4", "Chill log") # should be skipped
    
    engine.add_to_priority_alerts(log_w)
    engine.add_to_priority_alerts(log_c)
    engine.add_to_priority_alerts(log_e)
    engine.add_to_priority_alerts(log_i)
    
    # Assert size skipped INFO
    assert len(engine.priority_alerts) == 3
    
    # Check prioritization pop order
    assert engine.resolve_highest_priority_alert()[1] == "CRITICAL"
    assert engine.resolve_highest_priority_alert()[1] == "ERROR"
    assert engine.resolve_highest_priority_alert()[1] == "WARNING"
    assert engine.resolve_highest_priority_alert() is None
