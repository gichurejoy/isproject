from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class learner(models.Model):
    """Model representing an author."""
    AssessmentNumber = models.CharField(_("Assessment Number"),max_length=30,primary_key=True)
    FullName= models.CharField(_("Full Name"),max_length=100)
    BirthCertificateNumber = models.CharField(_("Birth Certificate Number"),max_length=30)
    Gender = models.CharField(_("Gender"),max_length=1)
    YearOfBirth = models.IntegerField(_("YearOfBirth"))

    class Meta:
        ordering = ['AssessmentNumber', 'FullName']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('learner-detail', args=[str(self.AssessmentNumber)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.AssessmentNumber}, {self.FullName}'

class instructor(models.Model):
    """Model representing an author."""
    IdNumber = models.IntegerField(_("ID Number"),max_length=30)
    FullName= models.CharField(_("Full Name"),max_length=100)
    Specialization = models.CharField(_("Specialization"),max_length=100)
    Gender = models.CharField(_("Gender"),max_length=1)
    Email = models.EmailField(_("Email"),max_length=254)

    class Meta:
        ordering = ['id', 'FullName']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('instructor-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id}, {self.FullName}'