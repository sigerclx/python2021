from mylib.configRead import readConfig
import os,pymysql,subprocess,sys

class Backup:
    def __init__(self):
        self.mysqlpath = readConfig('mysql','path')
        self.mysqluser = readConfig('mysql', 'user')
        self.mysqlpassword = readConfig('mysql', 'password')
        self.mysqlhost = readConfig('mysql', 'host')
        self.mysqlport = readConfig('mysql', 'port')
        self.backuppath = readConfig('backup', 'backuppath')
        self.backupdatabases = readConfig('backup', 'backupdatabases')
        self.DISABLED_DATABASES = {'information_schema', 'mysql', 'performance_schema', 'sys'}
        #print(self.mysqlpath,self.mysqluser,self.mysqlpassword,self.mysqlhost,self.mysqlport,self.backuppath,type(self.backupdatabases))
        #sys.exit(0)

    def backupDirectory_not_exists(self):
        """
        判断给定目录是否存在，不存在则创建它

        Args:
            path: 提示目录不存在
        """
        if not os.path.exists(self.backuppath):
            print(self.backuppath,'备份目录不存在！')
            sys.exit(0)

    def create_mysql_conn(self,db='mysql'):
        """
        创建并返回一个mysql数据库连接

        Args:
            db: 要连接的数据库名称

        Returns:

        """
        conn = pymysql.connect(host=self.mysqlhost, port=self.mysqlport, user=self.mysqluser, password=self.mysqlpassword,
                               db='mysql')
        return conn

    def read_all_databases(self):
        """
        从数据库中读取全部数据库名称

        Returns:
            list,数据库名称列表
        """
        # logging.info('读取全部数据库名称...')
        conn = self.create_mysql_conn()
        cursor = conn.cursor()
        # 查询服务器上有哪些数据库
        cursor.execute('show databases')
        res = cursor.fetchall()
        databases = {item[0] for item in res}
        # 排除掉指定不备份的数据库
        databases = list(databases - self.DISABLED_DATABASES)
        cursor.close()
        conn.close()
        #logging.info('读取完毕，数据库列表如下：{}'.format(databases))
        return databases
    #
    def backup_database(self,database):
        """
        备份指定数据库的数据和表结构

        Args:
            database: 待备份的数据库名称
        """
        #logging.info('开始备份数据库 {}...'.format(database))
        # 通过调用mysqldump完成指定数据库的备份
        command = os.path.join(self.mysqlpath,'bin\mysqldump')+' -h'+self.mysqlhost+' -u'+self.mysqluser +' -p'+self.mysqlpassword+ ' --add-drop-database --databases {database} > {backup_path}/{database}.sql'.format(
            database=database,
            backup_path=self.backuppath)

        #print('command:',command)
        exit_code = subprocess.call(command, shell=True)
        # 判断命令是否正常执行，异常则直接抛出
        if exit_code != 0:
            raise Exception('在备份数据库的过程中出错，请检查！')
        #logging.info('数据库 {} 备份完毕！'.format(database))

    def backup(self):
        """
        读取全部数据库名称，并对这些数据库的数据和结构进行备份
        """
        # 检查备份路径是否存在，不存在提示创建
        self.backupDirectory_not_exists()




        # 读取全部待备份数据库名称
        databases = self.read_all_databases()

        # 读取配置文件里备份的目标数据库
        if self.backupdatabases:
            databases = self.backupdatabases
        # 逐个对数据库进行备份
        for database in databases:
            self.backup_database(database)
