# module cmd elem

def cmd_elem(content, element):
    text = content.find_all(element)
    response = element + " element(s):\n"

    for line in text:
        response += str(line) + '\n'
    response += "_____\n"
    return response

def cmd_elems(content, elements):
    response = ""

    for element in elements:
        response += cmd_elem(content, element)
    return response

def cmd_elem_attribute(content, element, attribute):
    text = content.find_all(element)
    response = element + " element(s), " + attribute + " :\n"

    for line in text:
        response += str(line.get(attribute)) + '\n'
    response += "_____\n"
    return response

def cmd_elem_attributes(content, elements, attribute):
    response = ""

    for element in elements:
        response += cmd_elem_attribute(content, element, attribute)
    return response