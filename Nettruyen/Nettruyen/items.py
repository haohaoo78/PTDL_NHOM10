import scrapy

class NettruyenItem(scrapy.Item):
    tieu_de = scrapy.Field()
    tac_gia = scrapy.Field()
    luot_danh_gia =scrapy.Field()
    Xep_hang = scrapy.Field()
    so_chuong = scrapy.Field()
    tom_tat = scrapy.Field()
    the_loai = scrapy.Field()
    nguoi_theo_doi = scrapy.Field()
    cap_nhat = scrapy.Field()
    trang_thai = scrapy.Field()
    luot_xem = scrapy.Field()

