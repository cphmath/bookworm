from context import bookworm

def test_checkouts_by_usage_class_data():
    data = bookworm.data.get_checkouts_by_usage_class()
    assert all(data.columns == ['month_date', 'usage_class', 'monthly_checkouts'])
    assert len(data) >= 84
    assert set(data['usage_class'].unique()) == set(['Digital', 'Physical'])
