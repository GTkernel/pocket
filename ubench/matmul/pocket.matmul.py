# https://gist.github.com/yrevar/942d3a0ac09ec9e5eb3a
# imagenet index label
from time import time, sleep
t1=time()
import os, sys
import logging
sys.path.insert(0, '/root/')
sys.path.insert(0, '/root/tfrpc/client')
from pocket_tf_if import TFDataType
from yolo_msgq import PocketMessageChannel
t2=time()


t3=time()
msgq = PocketMessageChannel.get_instance()
t4=time()

def configs():
    logging.basicConfig(level=logging.INFO, \
                        format='[%(asctime)s, %(lineno)d %(funcName)s | _MATMUL] %(message)s')

if __name__ == '__main__':
    t5=time()
    configs()
    t6=time()

    s = time()
    for i in range(1):
        msgq._matmultest(int(sys.argv[1]))
    e = time()
    logging.info(f'matmultest: {e-s}')
    while True:
        sleep(10)
    msgq.detach()