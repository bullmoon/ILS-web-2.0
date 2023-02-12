def get_data():
    data = [{'material': 'copper', 'thickness': 5},
            {'material': 'copper', 'thickness': 10},
            {'material': 'copper', 'thickness': 12}]
    return data

def get_breaker():
        br_type = [{'Type': 'Tmax', 'Model': 'T4', 'Current': '250'},
                   {'Type': 'Tmax', 'Model': 'T5', 'Current': '400/630'},
                   {'Type': 'Tmax', 'Model': 'T6', 'Current': '630/800/1000'},
                   {'Type': 'Tmax', 'Model': 'T7', 'Current': '800/1000/1250/1600'}]
        return br_type