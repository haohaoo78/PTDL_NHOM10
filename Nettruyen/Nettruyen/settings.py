# Scrapy settings for Nettruyen project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "Nettruyen"

SPIDER_MODULES = ["Nettruyen.spiders"]
NEWSPIDER_MODULE = "Nettruyen.spiders"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "Nettruyen (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 3  # Delay giữa các yêu cầu

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# SPIDER_MIDDLEWARES = {
#    "Nettruyen.middlewares.NettruyenSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# DOWNLOADER_MIDDLEWARES = {
#    "Nettruyen.middlewares.NettruyenDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
ITEM_PIPELINES = {
   "Nettruyen.pipelines.CSVDBNettruyenPipeline": 100,
   "Nettruyen.pipelines.JsonDBNettruyenPipeline": 200,
   "Nettruyen.pipelines.MongoDBNettruyenPipeline": 400,
   'Nettruyen.pipelines.KafkaProducerPipeline': 1, 
}

# Enable and configure the AutoThrottle extension (disabled by default)
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 0  # Delay ban đầu cho AutoThrottle
AUTOTHROTTLE_MAX_DELAY = 60    # Delay tối đa khi gặp độ trễ cao
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0  # Số lượng request song song
AUTOTHROTTLE_DEBUG = False  # Không hiển thị thông tin chi tiết AutoThrottle

# Enable and configure HTTP caching (disabled by default)
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
