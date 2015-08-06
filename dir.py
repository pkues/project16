import os

class Dirmanager(object):
#    def __init__(self):
#        self.cur_dir = os.getcwd()

    @staticmethod    
    def listdir(cur_dir):
        l = [("dir","..\\")]
        rawdir = os.listdir(cur_dir)
        l_dir = [["dir",x] for x in rawdir if os.path.isdir(cur_dir + "\\" + x)]
        l_doc = [["doc",x] for x in rawdir if os.path.isfile(cur_dir + "\\" + x)]
        l_dir.extend(l_doc)
        l.extend(l_dir)
        return l
        
    @staticmethod        
    def changedir(cur_dir,new_dir):
        #check newdir
        if new_dir == '..\\':
            dir = os.path.dirname(cur_dir)
        else:
            dir = cur_dir + "\\" + new_dir
        return dir