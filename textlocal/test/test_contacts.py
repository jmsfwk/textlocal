import unittest

import textlocal.contacts


class TemplateTest(unittest.TestCase):

    def test_template(self):
        title = 'title'
        body = 'body'
        template = textlocal.contacts.Template(title, body)
        self.assertEqual(template.title, title)
        self.assertEqual(template.body, body)


class GroupTest(unittest.TestCase):

    def test_group_with_only_name(self):
        name = 'name'
        group = textlocal.contacts.Group(name)
        self.assertEqual(group.name, name)
        self.assertEqual(group.id, None)
        self.assertEqual(group.size, None)

    def test_group_with_group_id(self):
        name = 'name'
        group_id = 1
        group = textlocal.contacts.Group(name, group_id)
        self.assertEqual(group.id, group_id)

    def test_group_with_size(self):
        name = 'name'
        size = 1
        group = textlocal.contacts.Group(name, size=size)
        self.assertEqual(group.size, size)


if __name__ == '__main__':
    unittest.main()
