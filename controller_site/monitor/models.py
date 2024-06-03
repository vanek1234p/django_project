from django.db import models


class ListJobs(models.Model):
    active = models.BooleanField(default=True)

    workshop_number = models.IntegerField()  # номер цеха
    creation_date = models.DateTimeField()  # дата
    name_model = models.CharField(max_length=200)  # имя модели
    name_order = models.CharField(max_length=200)  # имя заказа
    name_operation = models.CharField(max_length=200)  # имя операции
    number_operation = models.IntegerField()  # номер операции
    name_work_center_name = models.CharField(max_length=200)  # название рабочего центра
    full_name_of_the_workers = models.CharField(max_length=200)  # ФИО рабочих исполнителей

    @classmethod
    def create(cls, dct):
        list_jobs = cls(
            workshop_number=dct['workshop_number'],
            creation_date=dct['creation_date'],
            name_model=dct['name_model'],
            name_order=dct['name_order'],
            name_operation=dct['name_operation'],
            number_operation=dct['number_operation'],
            name_work_center_name=dct['name_work_center_name'],
            full_name_of_the_workers=dct['full_name_of_the_workers']
        )
        return list_jobs


class ListCompletedJobs(models.Model):

    workshop_number = models.IntegerField()  # номер цеха
    creation_date = models.DateTimeField()  # дата
    name_model = models.CharField(max_length=200)  # имя модели
    name_order = models.CharField(max_length=200)  # имя заказа
    name_operation = models.CharField(max_length=200)  # имя операции
    number_operation = models.IntegerField()  # номер операции
    name_work_center_name = models.CharField(max_length=200)  # название рабочего центра
    Full_name_of_the_workers = models.CharField(max_length=200)  # ФИО рабочих исполнителей
    time_of_the_master_call = models.DateTimeField()  # время вызова мастера
    time_of_the_controller_call = models.DateTimeField()  # время вызова контролёра
    full_name_of_the_master_who_called = models.CharField(max_length=200)  # ФИО вызвавшего мастера
    full_name_of_the_responding_controller = models.CharField(max_length=200)  # ФИО ответившего контролёра
    time_of_the_controller_response = models.DateTimeField() # время ответа контролёра
    # full_name_of_the_responding_controller = models.CharField(max_length=200) # ФИО ответившего контролёра
    full_name_of_the_controller_who_made_the_decision = models.CharField(max_length=200, null=True)  # ФИО принявшего решение контролёра
    time_of_the_controller_decision = models.DateTimeField() # время принятия решения контролёром
    CHOICES_SOLUTION = {
        'waiting for the controller': 'waiting for the controller',
        'accepted': 'accepted',
        'not accepted': 'not accepted',
        'defective': 'defective'
    }
    solution = models.CharField(max_length=200, choices=CHOICES_SOLUTION)  # статус сменного задания (решение)

