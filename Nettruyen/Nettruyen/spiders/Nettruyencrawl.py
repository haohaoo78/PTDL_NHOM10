import scrapy
from bs4 import BeautifulSoup
from lxml import etree
from Nettruyen.items import NettruyenItem

class NettruyenSpider(scrapy.Spider):
    name = 'nettruyen'
    allowed_domains = ['nettruyenww.com']
    start_urls = [f'https://nettruyenww.com/?page={page}' for page in range(2, 100)]

    def parse(self, response):
        response_text = response.text.encode('utf-8').decode('utf-8')
        soup = BeautifulSoup(response_text, 'html.parser')
        truyens = soup.find_all('figure', class_="clearfix")
        
        for truyen in truyens:
            link_chi_tiet = truyen.find("a", class_="jtip")['href']
            yield response.follow(link_chi_tiet, self.parse_detail)

    def parse_detail(self, response):
        item = NettruyenItem()
        response_text = response.text.encode('utf-8').decode('utf-8')
        chi_tiet_soup = BeautifulSoup(response_text, 'html.parser')
        dom = etree.HTML(str(chi_tiet_soup))

        item['tieu_de'] = dom.xpath('normalize-space(string(//h1[@class="title-detail"]))')
        item['tac_gia'] = dom.xpath('normalize-space(string(//li[@class="author row"]//p[@class="col-xs-8"]))')
        item['the_loai'] = ', '.join(dom.xpath('//li[@class="kind row"]//a/text()'))
        item['tom_tat'] = dom.xpath('normalize-space(string(//div[@class="shortened"]))')
        item['nguoi_theo_doi'] = dom.xpath('normalize-space(string(//b[@class="number_follow"]))')
        item['cap_nhat'] = dom.xpath('normalize-space(string(//time[@class="small"]))')
        item['trang_thai'] = dom.xpath('normalize-space(string(//li[@class="status row"]//p[@class="col-xs-8"]))')
        item['luot_xem'] = dom.xpath('normalize-space(string(//li[@class="row"]//p[@class="col-xs-8"]))')
        item['so_chuong'] = len(dom.xpath('//ul[@id="desc"]/li'))

        rating = dom.xpath('normalize-space(string(//span[@itemprop="aggregateRating"]))')
        if rating:
            try:
                rating_split = rating.split(' - ')
                item['Xep_hang'] = rating_split[0].split(': ')[1].split('/')[0]
                item['luot_danh_gia'] = rating_split[1].split(' ')[0]
            except IndexError:
                item['Xep_hang'] = None
                item['luot_danh_gia'] = None
        if item['cap_nhat']:
            cap_nhat_cleaned = item['cap_nhat'].replace('Cập nhật lúc: ', '').strip().split(' ')[0]
            date_parts = cap_nhat_cleaned.split('-')
            if len(date_parts) == 3:
                item['cap_nhat'] = f"{date_parts[0]}-{date_parts[1]}-{date_parts[2]}"
            else:
                item['cap_nhat'] = None
        
        item['cap_nhat'] = item['cap_nhat'].replace("[", "").replace("]", "")
        yield item
