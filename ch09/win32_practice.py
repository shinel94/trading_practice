import win32com.client.dynamic as win32client

explorer = win32client.Dispatch("InternetExplorer.Application")
explorer.Visible = True
explorer.Quit()

word = win32client.Dispatch('Word.Application')
word.Visible = True
word.Quit()

excel = win32client.Dispatch("Excel.Application")
excel.Interactive = False
excel.Visible = True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")
ws.Cells(1,1).Value = 'hello world'
wb.SaveAs(r'C:\Users\HY\Desktop\TradingPractice\trading_practice\result_file\text.xlsx')
excel.Quit()

wb = excel.Workbooks.Open(r'C:\Users\HY\Desktop\TradingPractice\trading_practice\result_file\text.xlsx')
ws = wb.ActiveSheet
print(ws.Cells(1,1).Value)

ws.Cells(1,2).Value = 'is'
ws.Range('C1').Value = 'good'
ws.Range('C1').Interior.ColorIndex = 10
ws.Range('A1:F4').Interior.ColorIndex = 11
wb.SaveAs(r'C:\Users\HY\Desktop\TradingPractice\trading_practice\result_file\text.xlsx')

excel.Quit()