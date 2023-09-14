import base64

from icrawler import ImageDownloader
from icrawler.builtin import GoogleImageCrawler
from six.moves.urllib.parse import urlparse


# Solution for changing filenames copied directly from here:
# https://github.com/hellock/icrawler/issues/34#issuecomment-328320534
class MyImageDownloader(ImageDownloader):

    def get_filename(self, task, default_ext):
        url_path = urlparse(task['file_url'])[2]
        if '.' in url_path:
            extension = url_path.split('.')[-1]
            if extension.lower() not in [
                    'jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif', 'ppm', 'pgm'
            ]:
                extension = default_ext
        else:
            extension = default_ext
        # works for python3
        filename = base64.b64encode(url_path.encode()).decode()
        return '{}.{}'.format(filename, extension)


google_crawler = GoogleImageCrawler(
    downloader_cls=MyImageDownloader,
    downloader_threads=4,
    storage={"root_dir": "images"},
)
google_crawler.crawl(keyword="window photo", max_num=50)
google_crawler.crawl(keyword="window shutters", max_num=50)
google_crawler.crawl(keyword="window curtains", max_num=50)
google_crawler.crawl(keyword="awning window", max_num=50)
google_crawler.crawl(keyword="bay window", max_num=50)
google_crawler.crawl(keyword="bow window", max_num=50)
google_crawler.crawl(keyword="double hung window", max_num=50)
google_crawler.crawl(keyword="egress window", max_num=50)
google_crawler.crawl(keyword="fixed window", max_num=50)

