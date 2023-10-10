from django.db import models

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Flashcard(models.Model):
    question = models.TextField(help_text="Enter the question for the flashcard")
    image = models.ImageField(upload_to='flashcards/images/', blank=True, null=True, help_text="Upload an image if needed")
    file = models.FileField(upload_to='flashcards/files/', blank=True, null=True, help_text="Upload a file if needed")
    answer_text = models.TextField(blank=True, null=True, help_text="Enter the text answer for the flashcard")
    tags = models.ManyToManyField(Tag, blank=True, related_name="flashcards")

    def __str__(self):
        return self.question


class FlashcardAttempt(models.Model):
    flashcard = models.ForeignKey(Flashcard, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    was_correct = models.BooleanField()

