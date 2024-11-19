import scrapy
import pymongo
import json
import csv
import os
import subprocess
from scrapy.exceptions import DropItem

class MongoDBNettruyenPipeline:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = self.client['Nettruyendb_tho']

    def process_item(self, item, spider):
        collection = self.db['Truyens_tho'] 
        try:
            collection.insert_one(dict(item))  
            return item
        except Exception as e:
            raise DropItem(f"Error inserting item: {e}")
    def close_spider(self, spider):
        subprocess.run(["python", "data_spark.py"])

class JsonDBNettruyenPipeline:
    def __init__(self):
        self.file = open('nettruyen_data.json', 'w', encoding='utf-8')
        self.json_data = []

    def process_item(self, item, spider):
        self.json_data.append(dict(item))
        return item

    def close_spider(self, spider):
        json.dump(self.json_data, self.file, ensure_ascii=False, indent=4)
        self.file.close()

class CSVDBNettruyenPipeline:
    def __init__(self):
        self.file_path = 'Nettruyen_data.csv'
        self.file = open(self.file_path, 'a', encoding='utf-8-sig', newline='')
        self.writer = csv.writer(self.file)

        if os.stat(self.file_path).st_size == 0: 
            self.writer.writerow(['Tieu_de', 'Tac_gia', 'The_loai', 'Tom_tat', 
                                  'Nguoi_theo_doi', 'Cap_nhat', 'Trang_thai', 
                                  'Luot_xem', 'So_chuong', 'Xep_hang', 'luot_danh_gia'])

    def process_item(self, item, spider):
        self.writer.writerow([
            item['tieu_de'],
            item['tac_gia'],
            item['the_loai'],     
            item['tom_tat'],
            item['nguoi_theo_doi'],
            item['cap_nhat'],
            item['trang_thai'],
            item['luot_xem'],
            item['so_chuong'], 
            item['Xep_hang'], 
            item['luot_danh_gia'], 
        ])
        return item

    def close_spider(self, spider):
        self.file.close()
