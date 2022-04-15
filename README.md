# Money Manager

Money Manager program (Python based) for Computer programing project. 

## Tabel of content

* [About this program](#about-this-program)
* [Program Features](#program-features)
* [User Guide](#user-guide )
* [For Instructor](#for-instructor)
* [License](#license)

# About this program

โปรแกรมนี้มีจุดประสงค์เพื่อบันทึกรายรับรายจ่ายของผู้ใช้ และสามารถบันทึกข้อมูลเพื่อดูบันทึกย้อนหลัง หรือดูภาพรวมของการใช้จ่ายได้ เพื่อการจัดการและบริหารรายรับรายจ่ายอย่างมีประสิทธิภาพ นอกจากนี้ยังมี GUI (Graphic User Interface) และ คู่มือ (User manual) ที่ทำให้ผู้ใช้งานสามารถใช้งานได้ง่าย และเรียนรู้การใช้งานโปรแกรมได้ไวขึ้นอีกด้วย

โปรแกรมนี้ถูกเขียนขึ้นด้วยภาษา Python ทั้งการทำ Back-End และ Front-End มีฟังก์ชั่นการใช้งานรวมทั้งหมด 4 ฟังก์ชั่นหลัก สามารถบันทึกและอ่านข้อมูลโดยจะอยู่ในรูปแบบไฟล์นามสกุล .csv ที่สามารถนำไปใช้งานควบคู่กับโปรแกรม Microsoft Excel ได้ ฟังก์ชั่นหลักนั้นจะสามารถเขียนอธิบายออกมาได้ดังนี้

1.การบันทึกรายรับรายจ่าย ในส่วนของบันทึกรายรับรายจ่าย ผู้ใช้จะสามารถระบุ

วันที่ทำธุรกรรม เช่น ปัจจุบัน, ย้อนหลัง, ในอนาคต
ประเภทของธุรกรรม เช่น รายรับ,รายจ่าย
รายละเอียดธุรกรรม เช่น ค่าที่พัก, เงินเดือน
จำนวนเงิน
หลังจากกรอกรายละเอียดข้อมูลแล้วระบบจะบันทึกไว้ในที่เก็บข้อมูล ประเภท Dictionary และ List เพื่อให้ง่ายต่อการเก็บ และเรียกใช้งาน โดยใน Dictionary จะแบ่งออกเป็น 4 Keys เพื่อเก็บค่า ได้แก่ Date (วันที่), Category (รายละเอียด), Expense (จำนวนเงิน), Type (ประเภท) และในส่วนของ Value ใน Dictionary จะเก็บเป็นข้อมูลประเภท List

2.การบันทึก และโหลดข้อมูล ในส่วนของการบันทึก และโหลดข้อมูลนั้นทางผู้พัฒนาได้ใช้ไฟล์ประเภท .csv เพื่อให้ง่ายต่อการเขียน อ่าน และนำไปใช้ต่อ ในการบันทึกโปรแกรมจะทำการดึงข้อมูลจาก Dictionary ไปเขียนลงในไฟล์ .csv และทำการบันทึกไฟล์ เมื่อต้องการโหลดไฟล์ โปรแกรมจะทำการอ่านไฟล์ .csv ที่เลือก และนำข้อมูลมาแสดงในรูปแบบของ dataframe โปรแกรมนี้ผู้ใช้สามารถบันทึกไฟล์ในชื่อที่ต้องการได้ และสามารถอ่านไฟล์ที่เลือกจากที่ใดก็ได้ในเครื่องไม่จำเป็นต้องอยู่ในโฟลเดอร์เดียวกันกับโปรแกรม แต่ต้องอยู่ในรูปแบบของไฟล์ .csv

การเรียกกราฟรายจ่ายในแต่ละเดือน ผู้พัฒนาได้ทำฟังก์ชั่นเพื่อแสดงกราฟในโปรแกรม โดยอ่านค่าจากไฟล์ .csv แล้วบันทึกไว้ในรูปแบบ dataframe หลังจากนั้นจึงใช้ libary เพื่ออ่านค่าใน dataframe และนำมาพลอตกราฟ โดยในกราฟที่ได้จะมีการระบุ ประเภทของสิ่งที่จ่ายไปว่าสิ่งที่จ่ายไปนั้นคิดเป็นกี่ % ของรายจ่ายทั้งหมด เพื่อที่ผู้ใช้งานจะสามารถอ่าน และสังเกตได้ง่ายว่า ใช้จ่ายสิ่งใดมากกว่า หรือน้อยกว่ากัน

3.การเข้าดูประวัติรายรับรายจ่ายที่เคยบันทึกไว้ทั้งหมด

ในส่วนของการดูรายการธุรกรรมทั้งหมดที่เคยบันทึกไว้นั้น โปรแกรมจะอ่านค่าจากไฟล์ .csv และบันทึกไว้ในรูปแบบ dataframe หลังจากนั้นจึงนำมาแสดงผลในรูปแบบตารางบนตัวโปรแกรม

# Program Features

- Record your expenses in detail.
- Show percentage of monthly expenses as a Pie chart.
- Save file as csv.
- Load file and show all data records as a statics tabel.
- Easy to use GUI

# User Guide 

You can read user guide in About this program.md (TH version)

# For Instructor 
## Project Requirement and etc.

Requirements of the program 

1. User can enter income and expense using normal ledger format i.e.

   Date +Income/-Expense Description
   For example:

   1/5/2022 +22000 Salary 
 
   1/5/2022 -1500 Gas 
 
   1/5/2022 -350 Food 

2. Display summary daily or monthly using tabular form.
 
3. Easy to use. Program might need a menu for user interface.
 
# License
*Teams :*

 *1.Kanyanat Prapawesang* as main function developer
 
 *2.Punyada Adisaksodsai* as graphing and statistics function developer
 
 *3.Chakhriya Chantharakhami* as GUI developer 
 
*Major - Automation Robotics and Intelligence System Engineering*
