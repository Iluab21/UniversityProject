from datetime import datetime
from django.db.models import Count
from UniversityService.celery import app
from django.core.mail import EmailMessage
from UniversityService.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .models import Direction, StudyGroup
import xlwt
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def extract_db_and_send_email():
    logger.info('making report')

    # Making the directions info
    row_num = 0
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Directions')
    columns = ['Name', 'Discipline name', 'Curator name', 'Curator email', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])
    rows = Direction.objects.all().values_list('name', 'discipline__name',
                                               'curator__username', 'curator__email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]))

    # Making the students info
    ws = wb.add_sheet('Studygroups')
    row_num = 0
    columns = ['Student', 'Group', 'Phone number', 'Gender', 'Quantity in group with a same gender', 'Free places', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])

    data = []
    main_rows = StudyGroup.objects.all().values_list('student__name', 'name', 'student__phone', 'student__gender')\
        .order_by('student__name')
    genders = StudyGroup.objects.all().values('name', 'student__gender').annotate(count=Count('student__gender'))
    free = StudyGroup.objects.all().values('name').annotate(count=Count('student__id'))
    for i in main_rows:
        i = list(i)
        for j in genders:
            if i[1] == j['name']:
                if j['student__gender'] == i[3]:
                    i.append(j['count'])
        data.append(i)
    for i in free:
        for j in data:
            if j[1] == i['name']:
                j.append(20 - int(i['count']))

    for row in data:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]))

    # saving and sending report
    wb.save('report.xls')
    message = EmailMessage(f'Data as of {datetime.now().isoformat()}',
                           f'Generated at: {datetime.now().isoformat()}',
                           DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
    message.attach('report.xls', 'application/vnd.ms-excel')

    message.send()
