import xml.etree.ElementTree as ET

# 解析文件
tree = ET.parse("xmltest.xml")

# 获取根节点
root = tree.getroot()
# 打印节点标签
print(root.tag)

# # 遍历xml文档
# for child in root:
    # # 打印节点名和属性
    # print(child.tag, child.attrib)
    # # 遍历节点的子节点
    # for i in child:
        # print(i.tag, i.text)

# # 递归遍历子节点： year 节点
# for node in root.iter('year'):
    # print(node.tag, node.text)

# # 修改
# for node in root.iter('year'):
    # new_year = int(node.text) + 1
    # # 修改year节点的文本
    # node.text = str(new_year)
    # # 修改year节点的属性
    # node.set("updated", "yes")

# tree.write("xmltest.xml")

# 删除node
for country in root.findall('country'):
    print(country.tag)
    rank = int(country.find('rank').text)
    print(rank)
    if rank > 100:
        root.remove(country)

tree.write('output.xml')


def pretty_xml(element, indent, newline, level=0):  # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
    if element:  # 判断element是否有子元素    
        if (element.text is None) or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
            # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
            # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element)  # 将element转成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个    
            subelement.tail = newline + indent * level
        pretty_xml(subelement, indent, newline, level=level + 1)  # 对子元素进行递归操作



# import xml.etree.ElementTree as ET

# new_xml = ET.Element("namelist")
# # 给节点创建换行和缩进
# new_xml.text = '\n   '
# name = ET.SubElement(new_xml, "name", attrib={"enrolled": "yes"})
# # 给节点换行和缩进，节点的末尾换行
# name.text='\n'+'    '
# name.tail='\n'

# # 创建子节点，此节点的父节点是name
# age = ET.SubElement(name, "age", attrib={"checked": "no"})
# sex = ET.SubElement(name, "sex")
# sex.text = '33'
# name2 = ET.SubElement(new_xml, "name", attrib={"enrolled": "no"})
# age = ET.SubElement(name2, "age")
# age.text = '19'

# et = ET.ElementTree(new_xml)  # 生成文档对象
# et.write("test.xml", encoding="utf-8", xml_declaration=True)

# ET.dump(new_xml)  # 打印生成的格式
