'''
db 생성
CREATE DATABASE o2 CHARACTER SET utf8 COLLATE utf8_general_ci;

table 생성

CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` varchar(100) NOT NULL,
	`description` text NOT NULL,
	`author` varchar(30) NOT NULL,
	PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;

INSERT INTO `gangnam`.`topic` (`id`, `title`, `description`, `author`) VALUES ('2', 'dsa', 'dsds', 'dss');


UPDATE `gangnam`.`topic` SET `title` = '자gdfgdf' WHERE (`id` = '2');

DELETE FROM `gangnam`.`topic` WHERE (`id` = '2');
'''

import pymysql
db = pymysql.connect(
    host='localhost', 
    user='root', 
    password='1234', 
    db='gangnam',
    charset='utf8mb4')

cur = db.cursor()

#query = "SELECT * FROM topic"
#cur.execute(query)
#db.commit()

#data = cur.fetchall()

#print(data[0][1])


query = 'INSERT INTO `gangnam`.`topic` (`id`, `title`, `description`, `author`) VALUES (3 ,"자바" ,"처음에는 가전제품 내에 탑재해 동작하는 프로그램을 위해 개발했지만 현재 웹 애플리케이션 개발에 가장 많이 사용하는 언어 가운데 하나이고, 모바일 기기용 소프트웨어 개발에도 널리 사용하고 있다. 현재 버전 15까지 출시했다.", "GARY");'


#query = 'UPDATE `gangnam`.`topic` SET `title` = "3233" WHERE (`id` = "2");'
#cur.execute(query)
#db.commit()

#db.close()

#query = 'DELETE FROM `gangnam`.`topic` WHERE (`id` = "2");'

cur.execute(query)
db.commit()

db.close()