from multiprocessing import Pool
import os

def fazer():
    pool = Pool(processes=os.cpu_count())
    return pool
