from rest_framework import viewsets, status, permissions, serializers
from raterapi.models import Game
from rest_framework.response import Response
from django.http import HttpResponseServerError
from .categories import CategorySerializer


class GameSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = Game
        fields = (
            "id",
            "title",
            "description",
            "designer",
            "release_year",
            "players_number",
            "play_time",
            "min_age",
            "categories",
        )


class GameViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            games = Game.objects.all()
            serializer = GameSerializer(games, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized instance
        """
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, many=False)
            return Response(serializer.data)
        except Exception as ex:
            return Response(
                {"Bruh... Do you even Game??": ex.args[0]},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def create(self, request):
        """Make a game, bruh.."""
        game = Game.objects.create(
            title=request.data.get("title"),
            description=request.data.get("description"),
            designer=request.data.get("designer"),
            release_year=request.data.get("release_year"),
            players_number=request.data.get("players_number"),
            play_time=request.data.get("play_time"),
            min_age=request.data.get("min_age"),
        )

        category_ids = request.data.get("categories", [])
        game.categories.set(category_ids)

        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
