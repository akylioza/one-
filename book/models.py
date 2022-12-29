from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Rating(models.Model):
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_rate')
    RATE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    rating = models.CharField(max_length=100, choices=RATE)

    def __str__(self):
        return self.rating

class BookComment(models.Model):
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_comm')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Expert(models.Model):
    OCCUPATION = (
        ('писатель', 'писатель'),
        ('критик', 'критик'),
        ('издатель','издатель')
    )
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100, choices=OCCUPATION)
    info = models.TextField()

    def __str__(self):
        return self.name
class ExpertRecomendation(models.Model):
    book_choice = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_recomendation')
    text = models.TextField()
    expert_choice = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='expert_name')
    def __str__(self):
        return self.text