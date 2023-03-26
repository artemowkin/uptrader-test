from django.urls import reverse
from django.db import models


class Menu(models.Model):
    title: str = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class MenuItem(models.Model):
    menu: Menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    root_item: 'MenuItem' = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    title: str = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} (ID: {self.pk})"

    def get_absolute_url(self):
        return reverse('menus_list') + f'?menu{self.menu.id}={self.id}'
