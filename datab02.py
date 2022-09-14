def insert(RollNo, StudName, MathMarks, PhyMarks, CheMarks):
 import sqlite3
 con = sqlite3.connect('DetailsStud02.db')
 cur = con.cursor()
 RollNo = input("Enter RollNo = ")
 StudName = input("Enter Student Name = ")
 MathMarks = input("Enter Math Marks = ")
 PhyMarks = input("Enter Phy Marks = ")
 CheMarks = input("Enter Che Marks = ")

 cur.execute('''INSERT INTO DetailsSTUD02 (RollNo, StudName,MathMarks, PhyMarks, CheMarks) VALUES(?,?,?,?,?)''', (RollNo, StudName,MathMarks, PhyMarks, CheMarks))
 con.commit()
 con.close()


def fetch ():
    import sqlite3
    con = sqlite3.connect('DetailsStud02.db')
    cur = con.cursor()
    data = cur.execute('''select * from DetailsStud02''')
    for row in data:
        RollNo = row[0]
        StudName = row[1]
        MathMarks = row[2]
        PhyMarks = row[3]
        CheMarks = row[4]

        print(str(RollNo) + "  ,  " + StudName + " ,  " + str(MathMarks) + " ,  " + str(PhyMarks) + "  , " + str(CheMarks))



def update (RollNo,MathMarks):
    import sqlite3
    con = sqlite3.connect('DetailsStud02.db')
    cur = con.cursor()
    RollNo = input("Enter RollNo which you want to update = ")
    MathMarks = input("Enter Math Marks which you want to update  = ")
    data = cur.execute('''UPDATE DetailsStud02 set MathMarks = ?''' '''where RollNo = ?''', (MathMarks, RollNo,))
    con.commit()
    con.close()

def delete (RollNo):
    import sqlite3
    con = sqlite3.connect('DetailsStud02.db')
    cur = con.cursor()
    RollNo = input("Enter Roll which you want to delete = ")
    data = cur.execute('''delete from DetailsStud02 where RollNo = ?''', (RollNo, ))
    con.commit()
    con.close()


choice = 9
while (choice != 0):
    print('Enter 1 for INSERT ')
    print('Enter 2 for FETCH ')
    print('Enter 3 for UPDATE ')
    print('Enter 4 for DELETE ')
    print('')
    print('Enter 0 to exit')
    print('')
    choice = int(input('Enter Your Choice : '))
    if choice == 1:
        print(insert('val1', 'val2', 'val3', 'val4', 'val5'))
    elif choice == 2:
        print(fetch())
    elif choice == 3:
        print(update('RollNo', 'MathMarks'))
    elif choice == 4:
        print(delete('RollNo'))


