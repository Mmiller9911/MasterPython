# Simple rules:
#
# A "owns" B = Composition : B has no meaning or purpose in the system without A
# A "uses" B = Aggregation : B exists independently (conceptually) from A
#
# Composition is an Association
# Aggregation is an Association
# Composition is a strong Association (If the life of contained object totally depends on the container object, it is called strong association)
# Aggregation is a weak Association (If the life of contained object doesn't depends on the container object, it is called weak association)


class Tag(object):  # the other classes inherit from this one so the program uses inheritance

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return '{0.start_tag}{0.contents}{0.end_tag}'.format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag): # doctype IS-A tag

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd','')
        self.end_tag = '' # DOCTYPE doesn't have an end tag


class Head(Tag):

    def __init__(self):
        super().__init__('head', '')
        self.header_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self.header_contents.append(new_tag)

    def display(self, file=None):
        for tag in self.header_contents:
            self.contents += str(tag)

        super().display(file=file)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')
        self.body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self.body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self.body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):

    def __init__(self, doc_type, header, body):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def add_tag(self, name, contents, location):
        if location == 'body':
            self._body.add_tag(name, contents)
        else:
            self._head.add_tag(name, contents)
        # this just delegates the job to the body class method

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('<html>', file=file)


if __name__ == '__main__':

    new_body = Body()
    new_body.add_tag('h1', 'header')
    new_body.add_tag('p', "unlike <strong>composition</strong>, aggregation uses existing instances"
                          "of objects to build another object")
    new_body.add_tag('p', "the new object doesnt own the objects it is composed of"
                          "if it is destroyed the objects will continue to exist")

    new_doctype = DocType()
    new_header = Head()
    my_page = HtmlDoc(new_doctype, new_header, new_body)

    with open('test3.html', 'w') as file_doc2:
        my_page.display(file=file_doc2)