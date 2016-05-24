from time import sleep

from celery import shared_task
from celery.utils.log import get_task_logger

from seresults import parsers
from seresults.models import SE_GOOGLE, SE_BING

logger = get_task_logger(__name__)


@shared_task
def find_results(search_request):
    logger.info('START: ' + str(search_request))

    if search_request.search_engine == SE_GOOGLE:
        fetcher = parsers.fetch_aol
    elif search_request.search_engine == SE_BING:
        fetcher = parsers.fetch_aol
    else:
        return search_request

    sleep(15)

    raw_results = fetcher(search_request.query)

    logger.info('FINISHED: ' + str(search_request))

    search_request.finish(raw_results)
    return search_request


@shared_task(name='seresults.tasks.periodic')
def periodic():
    logger.info('PERIODIC')
