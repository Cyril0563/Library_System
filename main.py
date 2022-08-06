'''
#校园图书管理系统（学生可直接用作毕设或结课作业,不用和我联系（非商业））
#开源地址：https://github.com/Cyril0563/Library_System
#作者：Cyril0563
#时间：2022-08-06
'''


print("欢迎使用校园图书管理系统")
print("*** 1.录入图书信息 ***")
print("*** 2.查询图书信息 ***")
print("*** 3.删除图书信息 ***")
print("*** 4.修改图书信息 ***")
print("*** 5.退 出 系 统 ***")
print("请选择（1-5）：")
try:
    choice = int(input())
    if choice == 1:
        bookid = input("请输入图书编号：")
        bookname = input("请输入图书名称：")
        bookauthor = input("请输入图书作者：")
        bookprice = input("请输入图书价格：")
        booknum = input("请输入图书数量：")
        book = {'id': bookid, 'name': bookname, 'author': bookauthor, 'price': bookprice, 'num': booknum}
        with open('books.csv', 'a') as f:
            f.write(str(book) + '\n')
        print("图书信息录入成功！")
    elif choice == 2:
        print("请输入查询的图书编号：")
        bookid = input()
        with open('books.csv', 'r') as f:
            for line in f:
                book = eval(line)
                if book['id'] == bookid:
                    print("图书编号：" + book['id'])
                    print("图书名称：" + book['name'])
                    print("图书作者：" + book['author'])
                    print("图书价格：" + book['price'])
                    print("图书数量：" + book['num'])
                    break
                else:
                    print("没有找到该图书！")
    elif choice == 3:
        print("请输入删除的图书编号：")
        bookid = input()
        with open('books.csv', 'r') as f:
            lines = f.readlines()
        with open('books.csv', 'w') as f:
            for line in lines:
                book = eval(line)
                if book['id'] != bookid:
                    f.write(str(book) + '\n')
        print("图书信息删除成功！")
    elif choice == 4:
        print("请输入修改的图书编号：")
        bookid = input()
        with open('books.csv', 'r') as f:
            lines = f.readlines()
        with open('books.csv', 'w') as f:
            for line in lines:
                book = eval(line)
                if book['id'] == bookid:
                    print("请输入新的图书编号：")
                    bookid = input()
                    print("请输入新的图书名称：")
                    bookname = input()
                    print("请输入新的图书作者：")
                    bookauthor = input()
                    print("请输入新的图书价格：")
                    bookprice = input()
                    print("请输入新的图书数量：")
                    booknum = input()
                    book = {'id': bookid, 'name': bookname, 'author': bookauthor, 'price': bookprice, 'num': booknum}
                    f.write(str(book) + '\n')
                    print("图书信息修改成功！")
                else:
                    f.write(line)
    elif choice == 5:
        print("感谢使用，再见！")
        exit()
except ValueError:
    print("输入错误，请重新输入")
    choice = int(input())

