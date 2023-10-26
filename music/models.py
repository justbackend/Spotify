from django.db import models

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=150)
    tugilgan_yil = models.DateField()
    davlat = models.CharField(max_length=150)

    def __str__(self):
        return self.ism

class Albom(models.Model):
    nom = models.CharField(max_length=150)
    sana = models.DateField()
    rasm = models.FileField(upload_to='media')
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Qoshiq(models.Model):
    nom = models.CharField(max_length=150)
    janr = models.CharField(max_length=150)
    davomiylik = models.CharField(max_length=150)
    fayl = models.FileField(upload_to='music')
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

