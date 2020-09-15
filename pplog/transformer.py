import jq

def transform(data, query):
    try:
        return next(iter(jq.compile(query).input(data).all()), None)
    except ValueError:
        return data
