'''
Ushbu dastur yordamida IP-manzil orqali joyni aniqlash mumkin
Shuningdek, joyning geografik kengligi va uzunligini ham hisoblab beradi
Buning uchun ip-manzilni 0.0.0.0 formatda kiritish kifoya:)
Ushbu dastur ishlashi uchun ip2geotools modulini o`rnatish kerak bo`ladi.

pip install ip2geotools

Ushbu modul va uning funksiyalari haqida help(ipgeotools) orqali ma'lumot olish mumkin.


ESLATMA!

ip2geotools modulini pythonning 3.3 versiyasidan boshlab qo`llab-quvvatlaydi
'''
from ip2geotools.databases.noncommercial import DbIpCity

# IP-manzilni kiritamiz va uni satr ko`rinishiga o`tkazamiz
# Aynan satrli ko`rinishga o`tkazamiz, int yoki tuple ko`rinishga emas!
ip = str(input("IP manzilni kiriting:"))

# Googlening erkin API kaliti yordamida ushbu IP-manzil qaysi shaharga tegishli ekanini aniqlaymiz
response = DbIpCity.get(ip, api_key="free")

# Joyning geografik ma'lumotlarini ekranga chiqaramiz
print(response.city, response.region, response.country)
print(response.latitude, response.longitude)

'''
Ma'lumotlarni json, xml yoki csv formatda ham chiqarish mumkin.
Buning uchun mos ravishda
response.to_xml
response.to_json
response.to_csv
buyruqlaridan foydalanish mumkin.
'''
