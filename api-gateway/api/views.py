from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class BookSearchView(APIView):
    def get(self, request):
        query = request.GET.get("q")
        google_books = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={query}").json()
        results = []
        for item in google_books.get("items", []):
            volume = item["volumeInfo"]
            results.append({
                "title": volume.get("title"),
                "authors": volume.get("authors", []),
                "description": volume.get("description", ""),
                "isbn": volume.get("industryIdentifiers", [{}])[0].get("identifier", ""),
                "cover_image": volume.get("imageLinks", {}).get("thumbnail", ""),
            })
        return Response(results)