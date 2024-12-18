import psycopg2

try:
    # пытаемся подключиться к базе данных
    conn1 = psycopg2.connect(dbname='abdm_portal', user='postgres', password='p@ssword', host='10.10.57.242',
                             port='5432')
    conn2 = psycopg2.connect(dbname='fda_main', user='postgres', password='p@ssword', host='10.10.1.13',
                             port='5432')
except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
    print('Can`t establish connection to database')

cursor1 = conn1.cursor()
cursor2 = conn2.cursor()

cursor1.execute('SELECT chat.supporttasks.id, chat.supporttasks.datepost, chat.supporttasks.tasktype,'
                'chat.supporttasks.body, chat.supporttasks.dateclosed, concat(public.userprofile.userfname, %s, '
                'public.userprofile.userlname, %s, public.userprofile.usermname), public.userprofile.userid'
                ' FROM chat.supporttasks, public.userprofile WHERE datepost > %s AND '
                'chat.supporttasks.userid = public.userprofile.userid ORDER BY datepost DESC',
                (' ', ' ', '2024-03-01 00:00:00.000',))
cursor2.execute('SELECT kor, snam FROM public.s_sorg')

select1 = cursor1.fetchall()
select2 = cursor2.fetchall()

cursor1.close()
cursor2.close()

conn1.close()
conn2.close()

a = [v[6] for v in select1]
b = [v[0] for v in select2]

select1 = list(select1)

for a in b:
    a.pop(0)


#print(select1, '\n', select2)
#print(a, '\n', b)
print(a)
