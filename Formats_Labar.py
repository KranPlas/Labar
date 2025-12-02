import sqlite3, json, csv, os
if not os.path.exists('out'):
    os.makedirs("out")

connection = sqlite3.connect("labar.db")
cursor = connection.cursor()

cursor.execute('''
    SELECT 
        PCs.pc_id,
        PCs.name,
        PCs.user,
        PCs.program,
        PCs.inst_place,
        Users.name,
        Programs.name
    FROM PCs
    LEFT JOIN Users ON PCs.user = Users.user_id
    LEFT JOIN Programs ON PCs.program = Programs.software_id
    ''')

data = cursor.fetchall()

#JSON
json_data = []
for i in data:
    json_data.append({
        'id': i[0],
        'name': i[1],
        'user': i[2],
        'program': i[3],
        'inst_place': i[4],
    })
with open('out/data.json', 'w') as f:
    json.dump(json_data, f, indent=2)

#CSV
with open('out/data.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['ID', 'Name', 'User', 'Programs', 'Inst Place'])
    for row in data:
        writer.writerow([row[0], row[1], row[2], row[3], row[4]])

#XML
xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n<PCs>\n'
for i in data:
    xml_content += f'''  <pcs>
    <id>{i[0]}</id>
    <name>{i[1]}</name>
    <user>{i[2]}</user>
    <software>
        <program>{i[3]}</program>
        <inst_place>{i[4]}</inst_place>
    </software>
  </pcs>\n'''
xml_content += '</PCs>'
with open('out/data.xml', 'w') as f:
    f.write(xml_content)

#YAML
yaml_content = ''
for i in data:
    yaml_content += f'''- id: {i[0]}
  name: {i[1]}
  user: {i[2]}
  software:
    program: {i[3]}
    inst_place: {i[4]}\n'''
with open('out/data.yaml', 'w') as f:
    f.write(yaml_content)

print("Создание файлов")
connection.close()