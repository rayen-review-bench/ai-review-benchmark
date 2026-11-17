def paginate(items, page, per_page=10):
    start = (page - 1) * per_page
    return items[start:start + per_page]


def average(values):
    if not values:
        return 0.0
    return sum(values) / len(values)


def read_config(path):
    with open(path) as f:
        return dict(line.strip().split("=", 1) for line in f if "=" in line)