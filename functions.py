'''
Created on Sep 3, 2016

@author: anatoly
'''

import MySQLdb
import xml.etree.ElementTree as etree


class Mysql_(object):
    '''
    Класс для работы с БД
    '''
    def __init__(
            self,
            host = "",
            username = "",
            password = "",
            database = "",
            charset = "utf8"):
        '''
        Устанавливаем значения переменных
        '''
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.charset = charset
        self._tn_credit_card = u"credit_card"
        self._tn_types_calculations = u"types_calculations"

    def query(self,data):
        self.db = MySQLdb.connect(
                    host = self.host,
                    user = self.username,
                    passwd = self.password,
                    db = self.database,
                    charset = self.charset)
        self.cursor = self.db.cursor()
        self.cursor.execute(data)
        self.db.commit()
        self.db.close()
        return self.cursor.fetchall()

    def card_add(self,data):
        sql = """
                    INSERT
                        INTO %s (`NAME`)
                    VALUES ('%s')
                    """ % (self._tn_credit_card,data)
        return self.query(sql)

    def cards_get(self):
        sql = "SELECT `NAME` FROM %s" % (self._tn_credit_card)
        return self.query(sql)


    def card_delete(self,data):
        sql = "DELETE FROM %s WHERE (`NAME` = '%s')" % (self._tn_credit_card,data)
        self.query(sql)
        return 1

    # def card_exists(self,table=''):
    #   sql = "SHOW TABLES LIKE '{0}'".format(table)
    #   self.cursor.execute(sql)
    #   if len(self.cursor.fetchall()) > 0:
    #     return 1
    #   else:
    #     return 0
    
    def tables_create(self):
        self.query("CREATE TABLE IF NOT EXISTS %s (ID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(ID), NAME CHAR(25))") % (self._tn_credit_card)
        self.query("CREATE TABLE IF NOT EXISTS %s (ID INT NOT NULL AUTO_INCREMENT, PRIMARY KEY(ID), NAME CHAR(25))") % (self._tn_types_calculations)

    def tables_drop(self):
        self.query("DROP TABLE %s") % (self._tn_credit_card)
        self.query("DROP TABLE %s") % (self._tn_types_calculations)

    def table_list(self):
        sql = "SHOW TABLES"
        return self.query(sql)



class Xml_(object):
    
    def __init__(self,path):
        self.path = path
        self.name = ''
        self.dict = []
    
    # def __str__(self):
    #     return 'str: %s' % self.name
    
    # def __unicode__(self):
    #     return 'uni: %s' % self.name.decode('utf-8')

    # def __repr__(self):
    #     return 'repr: %s' % self.name


    def get_dict(self):
        for children in list(etree.parse(self.path).getroot()):
            if children.tag == 'SMS':
                if children.find('address').text == '900' and children.find('type').text != '2':
                    d = children.find('body').text.encode('utf-8')
                    self.dict.append({'date' : int(children.find('date').text) // 1000, 'body' : d})
        return self.dict

    def get_dict2(self):
        for children in list(etree.parse(self.path).getroot()):
            if children.tag == 'SMS':
                if children.find('body').text == 'Перевод 9272377860 100':
                    print (etree.tostring(children))
        return 1

    def match(self):
        return 1