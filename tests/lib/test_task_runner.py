from time import sleep

from tornado.testing import gen_test

from app.lib.cache import local_memoize
from app.lib.async import runner

@gen_test
def test_runner():
    @runner.async
    def slow():
        sleep(1)
        return 1
    ret = yield slow()
    assert ret == 1
