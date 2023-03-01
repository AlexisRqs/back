from django.db.models import Model, CharField, DateTimeField, IntegerField, ForeignKey, CASCADE


# Create your models here.
class Editor(Model):
    name = CharField(max_length=256)

class Game(Model):
    name = CharField(max_length=256)
    year = IntegerField()
    editor = ForeignKey(Editor, on_delete=CASCADE)

class Tournament(Model):
    title = CharField(max_length=256)
    date = DateTimeField()
    game = ForeignKey(Game, on_delete=CASCADE)