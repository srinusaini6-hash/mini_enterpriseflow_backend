from math import ceil


def paginate(query, page: int = 1, limit: int = 5):

    total = query.count()

    start = (page - 1) * limit

    results = query.offset(start).limit(limit).all()

    return {
        "total": total,
        "page": page,
        "limit": limit,
        "total_pages": ceil(total / limit),
        "data": results
    }