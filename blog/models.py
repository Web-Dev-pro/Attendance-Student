from django.db import models

# Create your models here.

class Team(models.Model):
    
    name = models.CharField(max_length=50)


    def	__str__(self):	
        return str(self.name)
    


class Worker(models.Model):
    fist_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=70)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="workers")
    
    def	__str__(self):
        return str(self.fist_name)
    
class Attendance(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField(auto_now_add=False)

    def __str__(self):
        return f"{str(self.team.name)} jamoaning {str(self.date)} sanasidagi ballari."
    

class Mark(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, related_name="mark")
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name="marks")
    is_attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ['attendance', 'worker']