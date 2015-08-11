# -*- coding: utf-8 -*-
import os

class DirManager(object):
    def __init__(self):
        self.cur_dir = os.getcwd().decode('utf-8')
 
    def listdir(self):
        l = [["dir","..\\"]]
        rawdir = os.listdir(self.cur_dir)
        l_dir = [["dir",x] for x in rawdir if os.path.isdir(self.cur_dir + "\\" + x)]
        l_doc = [["doc",x] for x in rawdir if os.path.isfile(self.cur_dir + "\\" + x)]
        l_dir.extend(l_doc)
        l.extend(l_dir)
        return l
              
    def changedir(self,new_dir):
        #check newdir
        if new_dir == '..\\':
            self.cur_dir = os.path.dirname(self.cur_dir)
        else:
            if self.cur_dir[-1] == '\\':
                self.cur_dir = self.cur_dir[:-1]
            self.cur_dir = self.cur_dir + "\\" + new_dir

class TableManager(object):
    def __init__(self):
        self.tables = []
    
    def get_name(self):
        return [x['name'] for x in self.tables]
    
    def get_path(self):
        return [x['path'] for x in self.tables]    
    
    def add_table(self,name,path):
        for table in self.tables:
            if table['name'] == name or table['path'] == path:
                return 0
        self.tables.append(({'name':name,'path':path}))
    
    def del_table(self,path):
        for table in self.tables:
            if table['path'] == path:
                self.tables.remove(table)
                return 1
        return 0
        
        
        
        