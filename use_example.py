import example_out.example_pb2 as addressbook_pb2

if __name__ == '__main__':
    person = addressbook_pb2.Person()
    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = addressbook_pb2.Person.HOME

    try:
        person.no_such_field = 1  # raises AttributeError
    except AttributeError as e:
        print("Generated {0} with args: {1}.".format(
            str(type(e)), str(e.args)
        ))
    try:
        person.id = "1234"  # raises TypeError
    except TypeError as e:
        print("Generated {0} with args: {1}.".format(
            str(type(e)), str(e.args)
        ))
    print('The generated object is:')
    print("Of type:{0}".format(str(type(person))))
    print("Repr as:\n{0}".format(repr(person)))
    print("Str as:\n{0}".format(str(person)))
    from pprint import pformat
    methods = [m for m in dir(person) if hasattr(person, m) and callable(getattr(person, m))]
    print("Has methods:\n{0}".format(pformat(methods)))
    print("Serialised into string as:{0}".format(person.SerializeToString()))
    try:
        print("\tWhich when decoded back is:{0}".format(person.SerializeToString().decode("ASCII")))
    except UnicodeDecodeError as e:
        print("I don't know how to decode the serialized string due to:{0}".format(str(e)))

    s = r"""name: "John Doe"
id: 1234
email: "jdoe@example.com"
phones {
  number: "555-4321"
  type: HOME
}"""
    print(addressbook_pb2.Person.ParseFromString(person.SerializeToString()))
    print(addressbook_pb2.Person.FromString(s))