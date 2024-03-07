import requests
import testxl

# def write_result(self, filename, sheetname, row, column, final_result):
#     wb = openpyxl.load_workbook(filename)
#     sheet = wb[sheetname]
#     sheet.cell(row=row, column=column).value = final_result
#     wb.save(filename)


def read_data(filename, sheetname):
    wb = testxl.load_workbook(filename)  # 加载工作薄
    sheet = wb[sheetname]
    max_row = sheet.max_row
    case_list = []

    for i in range(2, max_row + 1):
        dict1 = dict(
            case_id=sheet.cell(row=i, column=1).value,
            url=sheet.cell(row=i, column=2).value,
            data=sheet.cell(row=i, column=3).value,
            expect=sheet.cell(row=i, column=4).value
        )
        case_list.append(dict1)
    return case_list

cases = read_data("test_api.xlsx", "Sheet1")

print(cases)
# for case in cases:
#     case_id = case.get("case_id")
#     url = case.get("url")
#     method = case.get("method")
#     headers = case.get("headers")
#     data = case.get("data")
#     response = case.get("response")
#     msg = case.get("msg")
#     if method == "get":
#         real_msg = requests.get(url=url, headers=headers, data=data)
#
#     else:
#         real_msg = requests.post(url=url, headers=headers, data=data)
#     print("预期结果".format(msg))
#     print("实际结果".format((real_msg)))
#
#     if real_msg == msg:
#         print("第{}条用例通过".format(case_id))
#         final_re = "passed"
#     else:
#         print("第{}条用例不通过".format(case_id))
#         final_re = "failed"
#
#     write_result("test_api.xlsx", "Sheet1", 2, 7, final_re)
#
#
# if __name__ == '__main__':
#
#     print(cases)