# 엑셀로 바꾸어주지 않고 csv로 바꾸어준다. excel이 아닌 맥,구글스프레드시트같은 여러곳에서 사용 가능한 형태
# Comma Separated Value
# 각 cloumn을 ,로 나누어주며, row를 new line으로 구분.
# csv다루기
import csv


def save_to_file(jobs):

    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location"])
    for job in jobs:
        writer.writerow(list(job.values()))
    file.close()
