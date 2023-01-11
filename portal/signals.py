from django.db.models.signals import post_save
from django.contrib.auth.models import User 
from django.dispatch import receiver
from .models import Projects

@receiver(post_save,sender=Projects)
def editSkills(sender,instance,**kwargs):
    if instance.skills is not None and instance.skills != "":
        skill_list = instance.skills.split(",")
        new_str = ""
        for skill in skill_list:
            new_str += skill.strip()+","
        instance.skills = new_str[:-1]