'''
读取execl一列数据
'''
import xlrd  # pip install xlrd


class BbXls(object):
    def __init__(self, path):
        # 打开文件 获取工作簿名
        self.data = xlrd.open_workbook(path)
        self.sheet_name = self.data.sheet_names()
        # d定义数据表对象
        self.table = ''

    def get_table(self):
        # 获取 表名
        table = self.data.sheet_by_name(self.data_name[1])
        self.table = table

    def parse_data(self):
        # 解析数据
        data_col_list = self.table.col_values(0)
        data_str = ''
        for data_col in data_col_list:
            data_str += str(int(data_col)) + ','
        return data_str

    def save_file(self, data_str):
        # 保存文件
        with open('1.txt', 'w', encoding='utf-8') as f:
            f.write(data_str)

    def run(self):
        # 运行
        self.get_table()
        data_str = self.parse_data()
        self.save_file(data_str)


if __name__ == '__main__':
    path = './1.xls'
    bb = BbXls(path)
    bb.run()
