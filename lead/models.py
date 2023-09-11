from django.contrib.auth.models import User
from django.db import models


class Lead(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (CONTACTED, 'Contacted'),
        (WON, 'Won'),
        (LOST, 'Lost'),
    )

    name = models.CharField("имя", max_length=255)
    email = models.EmailField("почта")
    description = models.TextField("описание", blank=True, null=True)
    priority = models.CharField(max_length=10, choices=CHOICES_PRIORITY, default=MEDIUM, verbose_name='приоритет')
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=NEW, verbose_name='статус')
    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE, verbose_name='клиенты')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создано')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='изменено')

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name
