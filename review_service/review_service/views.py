
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

MOCK_REVIEWS = []

@csrf_exempt
def add_review(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        book_id = data.get("bookId")
        user_id = data.get("userId")
        rating = data.get("rating")
        comment = data.get("comment")

        if not all([book_id, user_id, rating, comment]):
            return JsonResponse({"error": "Missing fields"}, status=400)

        review = {
            "bookId": book_id,
            "userId": user_id,
            "rating": rating,
            "comment": comment
        }
        MOCK_REVIEWS.append(review)
        return JsonResponse({"message": "Review added successfully", "review": review}, status=201)

    return JsonResponse({"error": "Invalid method"}, status=405)


def get_book_reviews(request, book_id):
    if request.method == 'GET':
        book_reviews = [r for r in MOCK_REVIEWS if r["bookId"] == book_id]
        return JsonResponse({"reviews": book_reviews}, safe=False)

    return JsonResponse({"error": "Invalid method"}, status=405)
