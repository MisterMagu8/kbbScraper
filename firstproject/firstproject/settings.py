

BOT_NAME = 'kbb'
SPIDER_MODULES = ['kbb.spiders']
NEWSPIDER_MODULE = 'kbb.spiders'
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 0.5
ITEM_PIPELINES = {
    'kbb.pipelines.KbbPipeline': 300,
}