# from ouyeel.apiFuc import query_single_record, getCode, has_dic_attr
import xlrd, re, os
import datetime as dt
from .models import Mt


def read_mt_data(file_name, sheet):
    data = xlrd.open_workbook(file_name)
    table = data.sheet_by_name(sheet_name=sheet)
    name = table.name
    row_num = table.nrows  # 获取行数
    col_num = table.ncols  # 获取列数
    # print(table.cell_value(2,11))
    records = []
    for i in range(row_num):
        record = []
        try:
            if re.search(r"^\d{4}ZB-\d{4}", table.cell_value(i, 11)):
                for j in range(col_num):
                    record.append(table.cell_value(i, j))
                goodsInfoes = {
                    # 'publishPrice': self.publishPrice,
                    'balanceWeight': record[18],
                    'balanceQuantity': record[6],
                    'quantity': record[10],
                    'modiDate': date_strftime(float(record[2])),
                    'providerName': record[3],
                    'packCode': record[11],
                    'productName': "镀锡马口铁",
                    # 'onBusiness': self.shopSign,
                    # 'shopSign': self.shopSign,
                    'spec': record[5],
                    'spec1': record[14],
                    'spec3': record[15],
                    'spec5': record[16],
                    'specComment': record[8] + record[9],
                    'specialComments': record[13],
                    'storeCityName': "浙江台州",
                    'weight': record[12],
                    'driver': record[4],
                    # 'location': location,
                    # 'manufactureName': self.manufactureName,
                    # 'techStandard': self.techStandard,
                    # 'ticketRate': self.ticketRate,
                }
                records.append(goodsInfoes)
        except Exception as e:
            print("record without a code:", e)
            continue

    return records


def date_strftime(days):
    begin_date = dt.datetime(year=1899, month=12, day=30)
    date = begin_date + dt.timedelta(days=days)
    return date.strftime("%Y-%m-%d")


def update_mt_product(obj, i, updateNum):  # 麦铁库存数据更新修改
    num = 0
    for key in i.keys():
        if hasattr(obj, key):
            if str(i[key]) != obj.__getattribute__(key):
                obj.__setattr__(key, i[key])
                num += 1
    if num > 0:
        obj.save()
        updateNum += 1
    return updateNum


def work_on_mt(file_name, log_dir):
    sheet = "insert"
    records = read_mt_data(file_name=file_name, sheet=sheet)
    updateNum = 0
    insertNum = 0
    for i in records:
        try:
            if "packCode" in i:
                try:
                    # this record in db, then switch to next record
                    obj = Mt.objects.get(packCode=i["packCode"])
                    if obj:
                        updateNum = update_mt_product(obj, i, updateNum)
                        continue
                except Mt.DoesNotExist as e:
                    # print("%s does not exists!"%i['packCode'])
                    pass
                except Exception as e:
                    print("updating data Error", e)
                    continue
                obj = Mt(**i)
                obj.save()
                insertNum += 1

        except Exception as e:
            print("insertErr:", e, "\n", "packCode:", i["packCode"])

    timeStamp2 = dt.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    try:
        with open('%sinsertMt.txt' % log_dir, 'at', encoding='utf8') as f:
            if insertNum != 0:
                f.write("%s --insert records amounts %d \n" % (timeStamp2, insertNum))
        with open('%supdateMt.txt' % log_dir, 'at', encoding='utf8') as f:
            if updateNum != 0:
                f.write("%s --update records amounts %d \n" % (timeStamp2, updateNum))
    except Exception as e:
        print("write log error:", e)
    print("Data saved!")
    return insertNum, updateNum


if __name__ == '__main__':
    work_on_mt()


