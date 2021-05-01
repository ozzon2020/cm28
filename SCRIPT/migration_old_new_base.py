#from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pymysql
import random
from datetime import datetime
import time
import datetime

old_base = pymysql.connect(host='127.0.0.1', unix_socket='/var/run/mysqld/mysqld.sock', user='root', passwd='1111111', db='mysql', charset='utf8')
old = old_base.cursor()
old.execute("USE cm28old") # cur2
new_base = pymysql.connect(host='127.0.0.1', unix_socket='/var/run/mysqld/mysqld.sock', user='root', passwd='1111111', db='mysql', charset='utf8')
new = new_base.cursor()
new.execute("USE cm28") # curr1

#CREATE TABLE `postdoctor` (
  #`id` smallint(5) NOT NULL DEFAULT '0',
  #`idtheme` smallint(5) NOT NULL DEFAULT '0',
  #`datepost` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  #`name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '',
  #`theme` varchar(255) NOT NULL,
  #`email` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '',
  #`message` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  #`send` int(5) NOT NULL,
  #`answer` text NOT NULL,
  #`active` varchar(5) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  #`sort` int(10) NOT NULL DEFAULT '0'
#) ENGINE=MyISAM DEFAULT CHARSET=utf8;

#CREATE TABLE `questions_qs` (
  #`id` int(11) NOT NULL,
  #`theme` varchar(250) COLLATE utf8_bin DEFAULT NULL,
  #`main` longtext COLLATE utf8_bin NOT NULL,
  #`reply` longtext COLLATE utf8_bin,
  #`created` datetime(6) NOT NULL,
  #`updated` datetime(6) NOT NULL,
  #`sort` int(10) UNSIGNED NOT NULL,
  #`active` tinyint(1) NOT NULL,
  #`user_id` int(11) NOT NULL,
  #`total_likes` int(10) UNSIGNED NOT NULL,
  #`replyoff` tinyint(1) NOT NULL,
  #`doctor_id` int(11) NOT NULL,
#) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

#name2[0]
#qs(idc,theme,main,reply,sort,active)
def pr():
    print('Base start Pr!')
    
def __main__():
    print('Base start Main!')



    
def qs(idc,theme,main,reply,sort,active):
    us=()
    #cur2.execute("SELECT * FROM section WHERE namefile = %s",namefile)
    #section = cur2.fetchall() #2 
    cur1.execute("SELECT id FROM  auth_user" )
    users = cur1.fetchall() #2 
    for u in users:
        us+=u
        
    rand=random.randint(0, len(us)-1)    
    
    if active=='on':
        act=1
    else:
        act=0
        
    if reply !='':
        replyoff=1
    else:
        replyoff=0
        
    y=random.randint(2017, 2019)
    m=random.randint(1, 9)
    d=random.randint(10, 28)
    created=str(y)+'-0'+str(m)+'-'+str(d)+' 19:26:14.014176'    
    
    
    sql = "INSERT INTO questions_qs (id,theme,main,reply,created,updated,sort,active,user_id,total_likes,replyoff,doctor_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (idc,theme,main,reply,created,created,sort,act,us[rand],'0',replyoff,'2')
    print('\n\n'+str(val)+'\n-----------'+main+'\n user '+str(us[rand]))
    #print('\n\n'+str(section[0][0])+'\n-----------\n user '+str(us[rand]))

    cur1.execute(sql, val)    
    cur1.connection.commit()        
    
def comment(idc,namefile,main,active,sort):
    us=()
    cur2.execute("SELECT * FROM section WHERE namefile = %s",namefile)
    section = cur2.fetchall() #2 
    cur1.execute("SELECT id FROM  auth_user" )
    users = cur1.fetchall() #2 
    for u in users:
        us+=u
        
    rand=random.randint(0, len(us)-1)    
    
    if active=='on':
        act=1
    else:
        act=0
        
    y=random.randint(2015, 2019)
    m=random.randint(1, 9)
    d=random.randint(10, 28)
    created=str(y)+'-0'+str(m)+'-'+str(d)+' 19:26:14.014176'    
    
    
    sql = "INSERT INTO content_comment (id,body,created,modified,active,total_likes,section_id,user_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (idc,main,created,created,act,'0',section[0][0],us[rand])
    print('\n\n'+str(val)+'\n-----------'+main+'\n user '+str(us[rand]))
    #print('\n\n'+str(section[0][0])+'\n-----------\n user '+str(us[rand]))

    cur1.execute(sql, val)    
    cur1.connection.commit()        
    
    
    

def chast(idc,var_id,name,sort,active):
    if active=='on':
        act=1
    else:
        act=0
    sql = "INSERT INTO content_chast (id,name,sort,active,var_id) VALUES (%s,%s,%s,%s,%s)"
    val = (idc,name,sort,act,var_id)
    cur1.execute(sql, val)    
    cur1.connection.commit()    
    print(name+'\n------------------------\n');
    #CREATE TABLE `answer` (
      #`id` smallint(10) NOT NULL DEFAULT '0',
      #`idpolls` smallint(10) DEFAULT NULL,
      #`answer` varchar(255) DEFAULT NULL,
      #`rightanswer` varchar(5) NOT NULL,
      #`sort` smallint(5) NOT NULL DEFAULT '0',
      #`active` varchar(5) NOT NULL DEFAULT 'on'
    #) ENGINE=MyISAM DEFAULT CHARSET=utf8;    
    
    
    #CREATE TABLE `content_pollsanswed` (
      #`id` int(11) NOT NULL,
      #`name` varchar(250) COLLATE utf8_bin NOT NULL,
      #`right_answed` tinyint(1) NOT NULL,
      #`sort` int(10) UNSIGNED NOT NULL,
      #`active` tinyint(1) NOT NULL,
      #`polls_id` int(11) NOT NULL
    #) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;    
 #answed(name2[0],name2[2],name2[3],name2[4],name2[5],name2[1])   
def answed(ida,name,ra,sort,active,idpols):
    if active=='on':
        act=1
    else:
        act=0
        
    if ra=='1':
        r=1
    else:
        r=0
        
 
    
    sql = "INSERT INTO content_pollsanswed (id,name,right_answed,sort,active,polls_id) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (ida,name,r,sort,act,idpols)
    cur1.execute(sql, val)    
    cur1.connection.commit()    
    print(str(name)+'    \n------------------------\n');
    
    #CREATE TABLE `polls` (
      #`id` smallint(10) NOT NULL DEFAULT '0',
      #`name` varchar(250) DEFAULT NULL,
      #`idpageredirect` smallint(10) DEFAULT NULL,
      #`urlpage` varchar(255) NOT NULL,
      #`sort` smallint(5) NOT NULL DEFAULT '0',
      #`datepost` varchar(15) NOT NULL,
      #`colpolls` int(11) NOT NULL,
      #`active` varchar(5) NOT NULL DEFAULT 'on'
    #) ENGINE=MyISAM DEFAULT CHARSET=utf8;    
    
    
    #CREATE TABLE `content_polls` (
      #`id` int(11) NOT NULL,
      #`name` varchar(250) COLLATE utf8_bin NOT NULL,
      #`sort` int(10) UNSIGNED NOT NULL,
      #`active` tinyint(1) NOT NULL,
      #`redirect_id` int(11) NOT NULL,
      #`section_id` int(11) NOT NULL
    #) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;    
    #polls(name2[0],name2[1],name2[2],name2[3],name2[4],name2[7])
        
def polls(idp,name,redirect,url_page,sort,active):
    if active=='on':
        act=1
    else:
        act=0
    namefile=url_page.split('/')  
    cur2.execute("SELECT * FROM section WHERE namefile = %s",namefile[-1])
    section = cur2.fetchall() #2    
    
    sql = "INSERT INTO content_polls (id,name,sort,active,redirect_id,page_id) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (idp,name,sort,act,redirect,section[0][0])
    cur1.execute(sql, val)    
    cur1.connection.commit()    
    print(name+'  '+namefile[-1]+'  '+section[0][1]+' id : '+str(section[0][0])+'\n------------------------\n');

def razdel(idr,name,namefile,title,sort):
    #sort=sort*10
    #cur1.execute("INSERT INTO content_razdel (id,name,namefile,sort,block,block_active,created,active,image,main,about,meta_description,meta_keywords,stattex,title) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (idr,name,namefile,sort,name,1,'2019-10-30 08:34:53.595831','1',name,name,name,name,name,name,title))
    #cur1.connection.commit()

    sql = "INSERT INTO content_razdel (id,name,namefile,sort,block,block_active,created,active,image,main,about,meta_description,meta_keywords,stattext,title) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (idr,name,namefile,sort,name,1,'2019-10-30 08:34:53.595831','1',name,name,name,name,name,name,title)
    new.execute(sql, val)    
    new.connection.commit()
    print(name+namefile+'\n------------------------\n');
    #CREATE TABLE `content_razdel` (
      #`id` int(11) NOT NULL,
      #`name` varchar(200) COLLATE utf8_bin NOT NULL,
      #`namefile` varchar(100) COLLATE utf8_bin DEFAULT NULL,
      #`sort` int(10) UNSIGNED NOT NULL,
      #`block` longtext COLLATE utf8_bin,
      #`block_active` tinyint(1) NOT NULL,
      #`created` datetime(6) NOT NULL,
      #`active` tinyint(1) NOT NULL,
      #`image` varchar(100) COLLATE utf8_bin DEFAULT NULL,
      #`main` longtext COLLATE utf8_bin NOT NULL,
      #`about` longtext COLLATE utf8_bin NOT NULL,
      #`meta_description` varchar(250) COLLATE utf8_bin NOT NULL,
      #`meta_keywords` varchar(250) COLLATE utf8_bin NOT NULL,
      #`stattext` longtext COLLATE utf8_bin NOT NULL,
      #`title` varchar(250) COLLATE utf8_bin NOT NULL,
      
    #) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;


    #CREATE TABLE `section` (
      #`id` smallint(5) NOT NULL DEFAULT '0',
      #`namefile` varchar(50) NOT NULL,
      #`name` varchar(250) NOT NULL,
      #`title` varchar(250) DEFAULT NULL,
      #`meta_description` varchar(200) NOT NULL,
      #`meta_keywords` varchar(150) NOT NULL,
      #`main` longtext,
      #`imgpage` varchar(250) NOT NULL,
      #`polls` varchar(255) NOT NULL,
      #`dateraiting` varchar(50) NOT NULL,
      #`r` varchar(25) DEFAULT NULL,
      #`ch` smallint(5) DEFAULT NULL,
      #`countword` int(10) NOT NULL,
      #`recomend` varchar(5) NOT NULL,
      #`daterecomend` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
      #`raiting` int(10) NOT NULL,
      #`sort` smallint(5) DEFAULT NULL,
      #`colortr` varchar(50) NOT NULL,
      #`active` varchar(5) DEFAULT NULL
    #) ENGINE=MyISAM DEFAULT CHARSET=utf8;
    
    #CREATE TABLE `content_chast` (
      #`id` int(11) NOT NULL,
      #`name` varchar(200) COLLATE utf8_bin NOT NULL,
      #`sort` int(10) UNSIGNED NOT NULL,
      #`active` tinyint(1) NOT NULL,
      #`var_id` int(11) DEFAULT NULL
    #) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;   

def attr_replace(main,id):

    dd = BeautifulSoup(main, "html.parser")
    

    
    print('\n'+str(id)+'++++++++++++++++++++++++++++++++++++\n')
    pos=1
    for a in dd.find_all('img'):

        if a.attrs:
            a.attrs['src']=re.sub('/inc', '/static', a['src'])          

            #if pos == 1:
                #atrpos='right'
                #pos=0
            #else:
                #atrpos='left'
                #pos=1
            #if a.attrs['class']
            if 'class' in a.attrs:
                atrpos = a.attrs['class']  
                    
                a.attrs['class']='ui '+atrpos[0]+' floated image'
    
            del a['onclick']
            del a['style']

    for te in dd.find_all('table'):
        #del te.attrs
        for te1 in te.find_all('td'):
            if te1.attrs:
                del te1.attrs
        #if te:    
            #te.new_tag("table",attrs={"class": "ui celled table"})    
        #te.attrs['class']='ui celled table'
        te.attrs['class']='ui very basic table'


    #for te in dd.find_all('ul'):
        #del te.attrs
    for a in dd.find_all('h6'):
        a.name = 'p'
    
    for a in dd.find_all('h5'):
        a.name = 'strong'
    #for a in dd.find_all(re.compile('^h[1-6]$')):
        #del a.attrs
        
    for a in dd.find_all('strong'):
        a.replace_with(a.text)

    for a in dd.find_all('h1'):
            a.name = 'span'
            a.attrs['class']='h1'
    for a in dd.find_all('h2'):
            a.name = 'span'
            a.attrs['class']='h2'
    for a in dd.find_all('h3'):
            a.name = 'span'
            a.attrs['class']='h3'                    
    for a in dd.find_all('h4'):
            a.name = 'span'
            a.attrs['class']='h4'            
            
    return dd      
def razdelinsert(oldtb,newtb):
    
    CountRow=old.execute("SELECT * FROM  "+oldtb+"  ORDER BY id DESC")
    rows = old.fetchall()
    i=1
    for row in rows:
        sql = "INSERT INTO "+newtb+" (name,sort,active,var_id) VALUES (%s,%s,%s,%s)"
        val = (row[2],i,1,1)
        new.execute(sql, val)    
        new.connection.commit()   
        i+=1
        print('id {} name {}'.format(row[0],row[2]))    

        '''
        CREATE TABLE `content_section` (
  `id` int(11) NOT NULL,
  `name` varchar(250) COLLATE utf8_bin NOT NULL,
  `namefile` varchar(100) COLLATE utf8_bin NOT NULL,
  `title` varchar(250) COLLATE utf8_bin NOT NULL,
  `meta_description` varchar(250) COLLATE utf8_bin NOT NULL,
  `meta_keywords` varchar(250) COLLATE utf8_bin NOT NULL,
  `image` varchar(100) COLLATE utf8_bin DEFAULT NULL,
  `main` longtext COLLATE utf8_bin NOT NULL,
  `stattext` longtext COLLATE utf8_bin NOT NULL,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `sort` int(10) UNSIGNED NOT NULL,
  `active` tinyint(1) NOT NULL,
  `ch_id` int(11) DEFAULT NULL,
  `productlink_id` int(11) DEFAULT NULL,
  `sloganheader` longtext COLLATE utf8_bin NOT NULL,
  `top_page` longtext COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
'''
def section_replace(newtb,ids=None):
    
    if ids:
        CountRow=new.execute("SELECT * FROM  "+newtb+"  WHERE id="+str(ids)+"   ORDER BY id DESC")
    else:
        CountRow=new.execute("SELECT * FROM  "+newtb+"  ORDER BY id DESC")
            
    rows = new.fetchall()
    for row in rows:
        print('id {} name {} \n {}\n---------------\n'.format(row[0],row[2],row[7],))       
        
        #print(attr_replace(row[7],row[0])) 
        sql = "UPDATE content_section SET main=%s WHERE id=%s"
        val = (attr_replace(row[7],row[0]),row[0])
    
        new.execute(sql, val)  
        new.connection.commit()      
    print(CountRow)    
    
def sectioninsert(oldtb,newtb): 
    
    CountRow=old.execute("SELECT * FROM  "+oldtb+"  ORDER BY id DESC")
    rows = old.fetchall()
    ch=0
    for row in rows:
        if row[9]=='20': 
            ch=4
        elif row[9]=='21': 
            ch=3 
        elif row[9]=='22': 
            ch=2 
        else: 
            ch=1        
        
        sql = "INSERT INTO "+newtb+" (name,namefile,title,meta_description,meta_keywords,main,stattext,created,updated,sort,active,ch_id,sloganheader,top_page) \
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (row[2],row[1],row[3],row[4],row[5],row[9],row[2],'2019-10-30 08:34:53.595831','2019-10-30 08:34:53.595831',row[14],1,1,row[6],row[8])
        new.execute(sql, val)    
        new.connection.commit()   
    


        
        print('id {} name {} chast {}'.format(row[0],row[2],row[14]))        
    print(CountRow)
    
def olddata(datatable):
  

    CountRow=old.execute("SELECT * FROM  "+datatable+"  ORDER BY id DESC")
    rows = old.fetchall()
    for row in rows:
        print('id {} {} = {}'.format(row[0],row[1],row[2]))
    
     
        
    
    #CREATE TABLE `razdel` (
      #`id` smallint(5) NOT NULL DEFAULT '0',
      #`namefile` varchar(100) COLLATE utf8_bin NOT NULL,
      #`name` varchar(250) COLLATE utf8_bin NOT NULL DEFAULT '',
      #`sort` smallint(5) NOT NULL,
      #`active` varchar(5) COLLATE utf8_bin NOT NULL
    #) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin;    

    #CREATE TABLE `content_section` (
      #`id` int(11) NOT NULL,
      #`name` varchar(250) COLLATE utf8_bin NOT NULL,
      #`namefile` varchar(100) COLLATE utf8_bin NOT NULL,
      #`title` varchar(250) COLLATE utf8_bin NOT NULL,
      #`meta_description` varchar(250) COLLATE utf8_bin NOT NULL,
      #`meta_keywords` varchar(250) COLLATE utf8_bin NOT NULL,
      #`image` varchar(100) COLLATE utf8_bin DEFAULT NULL,
      #`main` longtext COLLATE utf8_bin NOT NULL,
      #`created` datetime(6) NOT NULL,
      #`updated` datetime(6) NOT NULL,
      #`sort` int(10) UNSIGNED NOT NULL,
      #`active` tinyint(1) NOT NULL,
      #`var_id` int(11) DEFAULT NULL,
      #`stattext` longtext COLLATE utf8_bin NOT NULL,
      #`ch_id` int(11) DEFAULT NULL
    #) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;  
    
def section_update(ids,namefile,name):
    sql = "UPDATE content_section SET name=%s,namefile=%s WHERE id=%s"
    val = (namefile,name,ids)
    print(name+namefile+' \n------------------------\n');
    cur1.execute(sql, val)  
    cur1.connection.commit()    
    
def section(ids,namefile,name,title,main,imgpage,var_id,ch_id,sort,active):
    #sort=sort*10
    if active=='on':
        act=1
    else:
        act=0
        
    im=''    
    im1=''    
    soup = BeautifulSoup(str(imgpage), 'html.parser')
    #for a in soup.find_all('img'):
    #im1=soup.findAll('img').get('src').text
    for a in soup.find_all('img'):
        im1=a['src']
        im=re.sub('/inc/images/', '', a['src'])  
    
    
    sql = "INSERT INTO content_section (id,name,namefile,title,meta_description,meta_keywords,image,main,created,updated,sort,active,var_id,stattext,ch_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (ids,name,namefile,title,name,name,im,main,'2020-01-15 08:34:53.595831','2020-01-15 08:34:53.595831',sort,act,var_id,name,ch_id)
    cur1.execute(sql, val)    
    cur1.connection.commit()
    print(name+namefile+' '+im1+'   '+im+'\n------------------------\n');
    #CREATE TABLE `content_razdel` (    
    
    
    #`id` int(11) NOT NULL, 34
    #`name` varchar(250) COLLATE utf8_bin NOT NULL,
    #`namefile` varchar(100) COLLATE utf8_bin NOT NULL,
    #`title` varchar(250) COLLATE utf8_bin NOT NULL,
    #`meta_description` varchar(250) COLLATE utf8_bin NOT NULL,
    #`meta_keywords` varchar(250) COLLATE utf8_bin NOT NULL,
    #`image` varchar(100) COLLATE utf8_bin DEFAULT NULL,
    #`main` longtext COLLATE utf8_bin NOT NULL,
    #`created` datetime(6) NOT NULL,
    #`updated` datetime(6) NOT NULL,
    #`sort` int(10) UNSIGNED NOT NULL,
    #`active` tinyint(1) NOT NULL,
    #`var_id` int(11) DEFAULT NULL,
    #`stattext` longtext COLLATE utf8_bin NOT NULL
def article(id,name,namefile,main,var_id,sort):
    sort=sort*10
    cur.execute("INSERT INTO content_article (id,name,namefile,title,meta_description,meta_keywords,main,created,updated,sort,active,var_id,stattext) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (id,name,namefile,name,name,name,main,'2019-10-25 08:34:53.595831','2019-10-25 08:34:53.595831',sort,'0',var_id,name))
    cur.connection.commit()
# 114  15

#nameDb=cur2.execute("SELECT * FROM oldsite_section WHERE active = '1' AND var_id='18' ORDER BY id DESC")
def pr2():
    print('Pr 2')


def themedoc(oldtb,newtb):
    
    CountRow=old.execute("SELECT * FROM  "+oldtb+"   ORDER BY id ASC")
    rows = old.fetchall()
    ch=0
    for row in rows:
      
        sql = "INSERT INTO "+newtb+" (id,name,sort,active) \
        VALUES (%s,%s,%s,%s)"
        val = (row[0],row[1],row[2],1)
        new.execute(sql, val)    
        new.connection.commit()      
        print('id {} name {} sort {} active {}'.format(row[0],row[1],row[2],row[3]))
        
def qs1(oldtb,newtb):
    
    CountRow=old.execute("SELECT * FROM  "+oldtb+"   ORDER BY id ASC")
    rows = old.fetchall()
    ch=0
    for row in rows:

        
        #CREATE TABLE `qs_qs` (
          #`id` int(11) NOT NULL,
          #`name` varchar(250) COLLATE utf8_bin NOT NULL,
          #`theme` varchar(250) COLLATE utf8_bin DEFAULT NULL,
          #`email` varchar(250) COLLATE utf8_bin NOT NULL,
          #`main` longtext COLLATE utf8_bin NOT NULL,
          #`reply` longtext COLLATE utf8_bin,
          #`created` datetime(6) NOT NULL,
          #`updated` datetime(6) NOT NULL,
          #`sort` int(10) UNSIGNED NOT NULL,
          #`replyoff` tinyint(1) NOT NULL,
          #`active` tinyint(1) NOT NULL,
          #`var_id` int(11) DEFAULT NULL
        #) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;  
        '''
        CREATE TABLE `qs_qs` (
  `id` int(11) NOT NULL,
  `name` varchar(250) COLLATE utf8_bin NOT NULL,
  `theme` varchar(250) COLLATE utf8_bin NOT NULL,
  `email` varchar(250) COLLATE utf8_bin NOT NULL,
  `main` longtext COLLATE utf8_bin NOT NULL,
  `reply` longtext COLLATE utf8_bin,
  `created` datetime(6) NOT NULL,
  `updated` datetime(6) NOT NULL,
  `sort` int(10) UNSIGNED NOT NULL,
  `replyoff` tinyint(1) NOT NULL,
  `active` tinyint(1) NOT NULL,
  `var_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
        '''        
        #CREATE TABLE `postdoctor` (
          #`id` smallint(5) NOT NULL DEFAULT '0',
          #`idtheme` smallint(5) NOT NULL DEFAULT '0',
          #`datepost` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '',
          #`name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '',
          #`theme` varchar(255) NOT NULL,
          #`email` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '',
          #`message` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
          #`send` int(5) NOT NULL,
          #`answer` text NOT NULL,
          #`active` varchar(5) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
          #`sort` int(10) NOT NULL DEFAULT '0'
        #) ENGINE=MyISAM DEFAULT CHARSET=utf8; 
        '''
        CREATE TABLE `postdoctor` (
  `id` smallint(5) NOT NULL DEFAULT '0',
  `idtheme` smallint(5) NOT NULL DEFAULT '0',
  `datepost` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '',
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '',
  `theme` varchar(255) NOT NULL,
  `email` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL DEFAULT '',
  `message` text CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `send` int(5) NOT NULL,
  `answer` text NOT NULL,
  `active` varchar(5) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `sort` int(10) NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
        '''

        timestamp = int(row[2])
        value = datetime.datetime.fromtimestamp(timestamp)
        
        sql = "INSERT INTO "+newtb+" (id,name,theme,email,main,reply,created,updated,sort,replyoff,active,var_id) \
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (row[0],row[3],row[4],row[5],row[6],row[8], \
               value.strftime('%Y-%m-%d %H:%M:%S'+'.595831'),value.strftime('%Y-%m-%d %H:%M:%S'+'.595831'),row[10],row[7],1,row[1])
        new.execute(sql, val)    
        new.connection.commit()    
        #row[2]

        #print(value.strftime('%Y-%m-%d %H:%M:%S'+'.595831'))        
        #print(time.strftime(row[2]))
        #print(time.strftime("Today is %B %d, %Y.", row[2]))
        print('id {} name {} sort {} active {}'.format(row[0],row[1],value.strftime('%Y-%m-%d %H:%M:%S'+'.595831'),row[3]))

if __name__ == "__main__":
        #olddata('section')
        #sectioninsert('section','content_section')
        #section_replace(newtb,ids=None):
        #razdelinsert('razdel','content_chast')
        #sectioninsert('section','content_section')
        #section_replace('content_section')
        #themedoc('themedoctor','qs_themeqs')
        qs1('postdoctor','qs_qs')

old_base.close()
old.close()