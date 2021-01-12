import jq

def transform(data, query):
    try:
        return jq.compile(query).input(data).all()
    except ValueError:
        return data
