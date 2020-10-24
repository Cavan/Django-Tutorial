from django.db import models
import datetime
from django.utils import timezone
from django.utils.timezone import now
# Create your models here.


class Question(models.Model):
    """[summary]

    :param models: [description]
    :type models: [type]
    :return: [description]
    :rtype: [type]
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    """[summary]

    :param models: [description]
    :type models: [type]
    :return: [description]
    :rtype: [type]
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# Django uses the following sql commands to create the above 
# models
# use command: python manage.py sqlmigrate polls 0001


# BEGIN;
# --
# -- Create model Question
# --
# CREATE TABLE "polls_question" (
#     "id" serial NOT NULL PRIMARY KEY,
#     "question_text" varchar(200) NOT NULL,
#     "pub_date" timestamp with time zone NOT NULL
# );
# --
# -- Create model Choice
# --
# CREATE TABLE "polls_choice" (
#     "id" serial NOT NULL PRIMARY KEY,
#     "choice_text" varchar(200) NOT NULL,
#     "votes" integer NOT NULL,
#     "question_id" integer NOT NULL
# );
# ALTER TABLE "polls_choice"
#   ADD CONSTRAINT "polls_choice_question_id_c5b4b260_fk_polls_question_id"
#     FOREIGN KEY ("question_id")
#     REFERENCES "polls_question" ("id")
#     DEFERRABLE INITIALLY DEFERRED;
# CREATE INDEX "polls_choice_question_id_c5b4b260" ON "polls_choice" ("question_id");

# COMMIT;